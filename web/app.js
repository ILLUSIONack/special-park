const express = require('express')
const app = express()
const port = 3000

// Express now knows that it should check the public folder for certain files
app.use(express.static("public"));
app.set("view engine", "ejs");

app.get("/", function(req, res){
    res.render("home");
})

app.get("/register", function(req, res){
    res.render("register");
})

app.get("/login", function(req, res){
    res.render("login");
})

app.post("/login", function(req, res) {
    
})


app.listen(port, function() {
    console.log(`Special park app listening at http://localhost:${port}`);
})