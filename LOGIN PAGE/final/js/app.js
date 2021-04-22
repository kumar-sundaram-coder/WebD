// var logIn = $("#li-1");
// var logInText = $(".login");
// var signUp = $("#li-2");
// var signUpText = $(".signup");
// var resetPass = $("#li-3");
// var resetPasswordText = $(".resetpassword");

const logIn = document.getElementById("li-1");
const logInText = document.querySelector(".login");
const signUp = document.getElementById("li-2");
const signUpText = document.querySelector(".signup");
const resetPass = document.getElementById("li-3");
const resetPasswordText = document.querySelector(".resetpassword");

logIn.addEventListener("click", () => {
  logIn.classList.remove("current");
  signUp.classList.remove("current");
  resetPass.classList.remove("current");
  logIn.classList.add("current");

  logInText.classList.remove("op-0");
  signUpText.classList.remove("op-0");
  resetPasswordText.classList.remove("op-0");
  logInText.classList.add("op-1");
  signUpText.classList.add("op-0");
  resetPasswordText.classList.add("op-0");
});
signUp.addEventListener("click", () => {
  logIn.classList.remove("current");
  signUp.classList.remove("current");
  resetPass.classList.remove("current");
  signUp.classList.add("current");

  logInText.classList.remove("op-0");
  signUpText.classList.remove("op-0");
  resetPasswordText.classList.remove("op-0");
  logInText.classList.add("op-0");
  signUpText.classList.add("op-1");
  resetPasswordText.classList.add("op-0");
});
resetPass.addEventListener("click", () => {
  logIn.classList.remove("current");
  signUp.classList.remove("current");
  resetPass.classList.remove("current");
  resetPass.classList.add("current");

  logInText.classList.remove("op-0");
  signUpText.classList.remove("op-0");
  resetPasswordText.classList.remove("op-0");
  logInText.classList.add("op-0");
  signUpText.classList.add("op-0");
  resetPasswordText.classList.add("op-1");
});
