const express = require('express');
const bodyParser = require('body-parser');
const axios = require('axios');
const cookieParser = require('cookie-parser');
const app = express();
const port = 3000;

// Express now knows that it should check the public folder for certain files

app.use(cookieParser("secretkey"));
app.use(bodyParser.urlencoded({extended: true}));
app.use(express.static("public"));
app.set("view engine", "ejs");

// Handle get requests
app.get("/", function (req, res) {
    if (req.signedCookies.Authorization) {
        res.redirect("dashbord");
    } else {
        res.render("home");
    }
});

app.get("/register", function (req, res) {
    if (req.signedCookies.Authorization) {
        res.redirect("dashbord");
    } else {
        res.render("register", {errorMessage: " "});
    }
});

app.get("/login", function (req, res) {
    if (req.signedCookies.Authorization) {
        res.redirect("dashbord");
    } else {
        res.render("login", {errorMessage: " "});
    }
});

app.get("/sign-out", function (req, res) {
    res.clearCookie("Authorization");
    res.redirect('/');
});

app.get("/dashbord", verifyToken, function (req, res) {
    res.render("dashbord")
});

app.get("/forgot-password", function (req, res) {
    if (req.signedCookies.Authorization) {
        res.redirect("dashbord");
    } else {
        res.render("forgot-password");
    }
});

app.get("*", function (req, res) {
    res.redirect("/")
});

// Authentication post requests
app.post("/register", function (req, res) {

    console.log("Request body:  ");
    console.log(req.body);

    const register_url = 'http://127.0.0.1:8000/users/registration/';

    const fullName = req.body.firstName + req.body.surName;
    console.log(fullName)
    const registeration_info = {
        username: fullName,
        email: req.body.email,
        password1: req.body.password1,
        password2: req.body.password2
    };

    // const registeration_info = {
    //     username: 'usmansiddiqui1',
    //     email: 'usmansiddiqui1@hotmail.com',
    //     password1: 'usmansiddiqui123',
    //     password2: 'usmansiddiqui123'
    // }

    console.log(registeration_info);

    axios.post(register_url, registeration_info)
        .then((result) => {
            console.log("registered user");
            res.redirect("login")
        }).catch((error) => {
        if (error.response) {
            // The request was made and the server responded with a status code
            // that falls out of the range of 2xx
            console.log(error.response);
            res.render("register", {errorMessage: error.response.data});
            console.log(error.response.status);
            console.log(error.response.headers);
        } else if (error.request) {
            console.log(error.request);
        } else {
            console.log('Error', error.message);
        }
        console.log(error.config);
    });
})

app.post("/login", function (req, res) {

    const login_url = 'http://127.0.0.1:8000/users/login/';

    // const login_information = {
    //     username: 'usmansiddiqui',
    //     email: "usmansiddiqui@hotmail.com",
    //     password: "usmansiddiqui123"
    // };

    const login_information = {
        username: 'usmansiddiqui',
        email: req.body.email,
        password: req.body.password
    };

    console.log(req.body);

    const response = async () => {
        try {
            const response = await axios.post(login_url, login_information);
            console.log(response.data);
            return response.data.key
        } catch (error) {
            if (error.response) {
                // The request was made and the server responded with a status code
                // that falls out of the range of 2xx
                console.log(error.response);
                res.render("login", {errorMessage: error.response.data});
                console.log(error.response.status);
                console.log(error.response.headers);
            } else if (error.request) {
                console.log(error.request);
            } else {
                console.log('Error', error.message);
            }
            console.log(error.config);
        }
    };

    response()
        .then((token) => {
            if (token !== undefined) {
                res
                    .cookie('Authorization', 'Token ' + token, {
                        expires: new Date(Date.now() + 8 * 3600000), signed: true
                    })
                    .redirect("/dashbord")
            }
        })
        .catch((error) => console.log('error: ', error))
});

function verifyToken(req, res, next) {
    const token = req.signedCookies.Authorization;
    if (token) {
        next()
    } else {
        res.redirect("login");
    }
}

app.listen(port, function () {
    console.log(`Special park app listening at http://localhost:${port}`);
});