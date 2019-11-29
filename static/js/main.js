console.log('Main js is active');

var loginDiv = document.querySelector('#login-div');
var loginBtn = document.querySelector('#login-btn');
var searchForm = document.querySelector('#search-form');

loginBtn.addEventListener("mouseover", () => {
    loginDiv.style.display = 'block';
    searchForm.style.display = 'none';
})