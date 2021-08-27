const express = require("express");
const bodyParser = require("body-parser");
const ejs = require("ejs");
const _ = require("lodash");

const posts = [];

const homeStartingContent =
  "Lorem ipsum dolor sit amet consectetur adipisicing elit. Itaque obcaecati, quisquam, laborum similique beatae perferendis tempora totam soluta eveniet earum debitis eligendi in quibusdam. Voluptatibus vero ad debitis cum molestias, quae est necessitatibus. Fuga voluptates ex fugit sed molestiae iusto debitis, perspiciatis laborum eius quibusdam dolor quia natus harum maiores?";
const aboutContent =
  "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Ducimus dignissimos cum nulla et voluptatibus minima, aspernatur, ea veniam laboriosam quibusdam mollitia perferendis! Velit ducimus facilis laboriosam ratione. At tempora quae soluta, fuga corporis id fugiat laudantium dolorem, harum labore assumenda!";
const contactContent =
  "Lorem ipsum dolor sit amet consectetur adipisicing elit. Incidunt totam dolor reprehenderit non quam. Esse ut, deleniti doloribus quas alias, ipsa accusamus ex cum mollitia, corporis consequuntur dolores provident quidem.Lorem ipsum dolor sit amet consectetur adipisicing elit. Incidunt totam dolor reprehenderit non quam. Esse ut, deleniti doloribus quas alias, ipsa accusamus ex cum mollitia, corporis consequuntur dolores provident quidem.";

const app = express();

app.set("view engine", "ejs");

//using bodyparser
app.use(bodyParser.urlencoded({ extended: true }));

// Using Static
app.use(express.static(__dirname + "/public"));

app.get("/posts/:postName", (req, res) => {
  let requiredName = _.lowerCase(req.params.postName);

  for (let obj of posts) {
    let objTitle = _.lowerCase(obj.title);
    if (objTitle === requiredName) {
      res.render("post", { Title: obj.title, Post: obj.post });
      // console.log("Match Found!!!");
      break;
    } else {
      console.log("No Match Found!");
    }
  }
});

app.get("/", (req, res) => {
  res.render("home", {
    startingContentHome: homeStartingContent,
    postsArray: posts,
  });
});

app.get("/about", (req, res) => {
  res.render("about", { contentAbout: aboutContent });
});

app.get("/contact", (req, res) => {
  res.render("contact", { contentContact: contactContent });
});

app.get("/compose", (req, res) => {
  res.render("compose");
});

app.post("/compose", (req, res) => {
  const completePost = {
    title: req.body.compose,
    post: req.body.textarea,
  };

  posts.push(completePost);
  res.redirect("/");

  // const completePost =
  //   "Title: " + req.body.compose + " Post: " + req.body.textarea;
  // console.log(req.body.compose);
  // res.write("<h1>Published</h1>");
  // res.write(completePost);
  // res.send();
});

// listen to the foloowing port i.e., 3000
app.listen(3000, () => {
  console.log("Server is running on Port 3000");
});
