from flask import Flask,render_template,request
from keras.models import load_model 
import pickle
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
from nltk.stem import SnowballStemmer
import pymongo
from bson.objectid import ObjectId

client = pymongo.MongoClient("mongodb+srv://admin:ilovecoding@cluster0.yy73e.mongodb.net/MovieReviewDB?retryWrites=true&w=majority")
movieReviewsDB = client["MovieReviewDB"]
movieReview = movieReviewsDB["MovieReview"]
feedbackCollection=movieReviewsDB["FeedbackCollection"]

# print(movieReview.find({}))

app=Flask(__name__)

tfidf=tfidf = pickle.load(open("tfidf.pkl", "rb" ) )
myRegExpTokenizer=RegexpTokenizer('[a-z]+')
sw=stopwords.words('english')
sb=SnowballStemmer('english')
sw.remove('not')

model=load_model("best_model.h5")
model.make_predict_function()

def classifyReview(movieReviews):
	movieReviews=list([movieReviews])
	# Do same preprocessing as done for testing data
	for i in range(len(movieReviews)):
	    sentence=movieReviews[i].lower()
	    sentence=myRegExpTokenizer.tokenize(sentence) # Tokenizing
	    sentence=[word for word in sentence if word not in sw] # Stopwords removing
	    for j in range(len(sentence)):
	        sentence[j]=sb.stem(sentence[j]) # Stemming
	    movieReviews[i]=' '.join(sentence)

	# Transform the given reviews for model
	movieReviews=tfidf.transform(movieReviews)

	movieReviews.sort_indices()
	pred=model.predict_classes(movieReviews)

	return pred[0]


@app.route("/",methods=['GET','POST'])
def homePage():
	return render_template("index.html")

@app.route("/addReview")
def addReviewPage():
	return render_template("addreview.html")


@app.route("/searchMovies")
def searchMoviesPage():
	foundMovie=movieReview.find()
	movieList=[]
	for movie in foundMovie:
		movieList.append({"movieName":movie["movieName"],"id":movie["_id"]})
	return render_template("searchmovies.html",movieList=movieList)

@app.route("/about")
def aboutPage():
	return render_template("about.html")

@app.route("/contact")
def contactPage():
	return render_template("contact.html")


@app.route("/submitReview",methods=['GET','POST'])
def submitReview():
	if request.method=='POST':
		review=request.form['review']
		name=request.form['name']
		movieName=request.form['Moviename'].upper()

		if name=="" or review=="" or movieName=="":
			return render_template("addreview.html",isEmpty=True)

		pred=classifyReview(review)
		prediction=""
		if pred==1:
			prediction="Positive"
		else:
			prediction="Negative"

		rating=0

		foundMovie=movieReview.find_one({"movieName":movieName})
		if foundMovie:
			foundMovie["reviewsList"].append({"name":name,"review":review,"prediction":prediction})
			foundMovie["totalReviews"]=foundMovie["totalReviews"]+1
			if prediction=="Positive":
				foundMovie["positiveReviews"]=foundMovie["positiveReviews"]+1
			rating=int((foundMovie["positiveReviews"]*5.0)/(foundMovie["totalReviews"]*1.0))
			foundMovie["rating"]=rating
			movieReview.update_one({"movieName":movieName},{"$set":foundMovie})
		else:
			posRev=0
			totalRev=1
			if prediction=="Positive":
				posRev=posRev+1
			rating=int((posRev*5.0)/(totalRev*1.0))
			movieReview.insert({"movieName":movieName,"rating":rating,"positiveReviews":posRev, "totalReviews":totalRev ,"reviewsList":[{"name":name,"review":review,"prediction":prediction}]})


		return render_template("addreview.html", name=name, movieName=movieName, review=review, rating=rating, prediction=prediction)


@app.route("/findMovie",methods=['GET','POST'])
def findMovie():
	if request.method=='POST':
		movieName=request.form['searchMovie'].upper()

	foundMovie=movieReview.find_one({"movieName":movieName})
	if not foundMovie:
		foundMovie="notFound"


	allMovies=movieReview.find()
	movieList=[]
	for movie in allMovies:
		movieList.append({"movieName":movie["movieName"],"id":movie["_id"]})


	return render_template("searchmovies.html",foundMovie=foundMovie,movieList=movieList)

@app.route("/findMovieFromList",methods=['GET','POST'])
def findMovieFromList():
	if request.method=='POST':
		movieID=request.form['searchMovie']

	foundMovie=movieReview.find_one({"_id":ObjectId(movieID)})
	
	if not foundMovie:
		foundMovie="notFound"


	allMovies=movieReview.find()
	movieList=[]
	for movie in allMovies:
		movieList.append({"movieName":movie["movieName"],"id":movie["_id"]})


	return render_template("searchmovies.html",foundMovie=foundMovie,movieList=movieList)


@app.route("/feedbackSubmitted",methods=['GET','POST'])
def feedbackSubmitted():
	if request.method=='POST':
		name=request.form['name']
		email=request.form['email']
		message=request.form['message']

	if name=="" or email=="" or message=="":
		return render_template("contact.html",isEmpty=True)

	feedbackCollection.insert_one({"name":name,"email":email,"message":message})
	return render_template("contact.html",submitted=True)


if __name__=="__main__":
	app.run(debug=True)
