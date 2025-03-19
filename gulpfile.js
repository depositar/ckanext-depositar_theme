const path = require("path");
const { src, watch, dest, parallel } = require("gulp");
const sass = require("gulp-sass")(require("sass"));
const if_ = require("gulp-if");
const sourcemaps = require("gulp-sourcemaps");

const with_sourcemaps = () => !!process.env.DEBUG;

const buildScss = () =>
  src([
    __dirname + "/ckanext/depositar_theme/fanstatic/scss/main.scss"
  ])
    .pipe(if_(with_sourcemaps(), sourcemaps.init()))
    .pipe(sass({
      outputStyle: 'expanded',
      includePaths: ['../ckan/ckan/public/base/']
    }).on('error', sass.logError))
    .pipe(if_(with_sourcemaps(), sourcemaps.write()))
    .pipe(dest(__dirname + "/ckanext/depositar_theme/fanstatic/styles/"));

const watchSource = () =>
  watch([
    __dirname + "/ckanext/depositar_theme/fanstatic/scss/**/*.scss"],
    { ignoreInitial: false },
    parallel(
      buildScss
    )
  );

exports.build = parallel(
  buildScss
);
exports.watch = watchSource;
