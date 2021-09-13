var express = require("express");
var path = require("path");
const { execSync } = require("child_process");
const fs = require("fs");
var app = express();

// view engine setup
app.set("views", path.join(__dirname, "views"));
app.set("view engine", "ejs");

app.use(express.static(path.join(__dirname, "public")));

const PORT = 3000;

var router = express.Router();

router.get("/", function (request, response) {
  response.render("index");
});

router.get("/fetch", function (request, response) {
  const { from, to, length, width, height, weight } = request.query;

  const cmd =
    'python scrape.py "' +
    from.trim() +
    '" "' +
    to.trim() +
    '" ' +
    length.toString() +
    " " +
    width.toString() +
    " " +
    height.toString() +
    " " +
    weight.toString() +
    " > output.txt";
console.log(cmd)
  var executing = require("child_process").execSync(cmd, {
    stdio: "ignore",
  });

  fs.readFile("output.txt", "utf8", (err, data) => {
    if (err) {
      console.error(err);
      return;
    }
    console.log(data);
    response.render("result", { data });
  });
});

app.use("/", router);

app.listen(PORT, function () {
  console.log("Listening on port " + PORT);
});
