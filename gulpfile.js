const path = require("path");
const { src, watch, dest, parallel } = require("gulp");
const sass = require("gulp-sass")(require("sass"));
const if_ = require("gulp-if");
const sourcemaps = require("gulp-sourcemaps");

const with_sourcemaps = () => !!process.env.DEBUG;

const buildMain = () =>
  src([
    __dirname + "/ckanext/depositar_theme/fanstatic/scss/main/main.scss"
  ])
    .pipe(if_(with_sourcemaps(), sourcemaps.init()))
    .pipe(sass({ outputStyle: 'expanded' }).on('error', sass.logError))
    .pipe(if_(with_sourcemaps(), sourcemaps.write()))
    .pipe(dest(__dirname + "/ckanext/depositar_theme/fanstatic/styles/"));

const buildIndex = () =>
  src(__dirname + "/ckanext/depositar_theme/fanstatic/scss/index/index.scss")
    .pipe(if_(with_sourcemaps(), sourcemaps.init()))
    .pipe(sass({ outputStyle: 'expanded' }).on('error', sass.logError))
    .pipe(if_(with_sourcemaps(), sourcemaps.write()))
    .pipe(dest(__dirname + "/ckanext/depositar_theme/fanstatic/styles/"));

const watchSource = () =>
  watch([
    __dirname + "/ckanext/depositar_theme/fanstatic/scss/**/*.scss"],
    { ignoreInitial: false },
    parallel(
      buildMain,
      buildIndex
    )
  );

exports.build = parallel(
  buildMain,
  buildIndex
);
exports.watch = watchSource;
