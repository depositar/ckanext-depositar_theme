const path = require("path");
const { src, watch, dest, parallel } = require("gulp");
const sass = require("gulp-sass")(require("sass"));
const less = require("gulp-less");
const if_ = require("gulp-if");
const sourcemaps = require("gulp-sourcemaps");

const with_sourcemaps = () => !!process.env.DEBUG;

const buildLess = () =>
  src(__dirname + "/ckanext/depositar_theme/fanstatic/less/index/index.less")
    .pipe(if_(with_sourcemaps(), sourcemaps.init()))
    .pipe(less())
    .pipe(if_(with_sourcemaps(), sourcemaps.write()))
    .pipe(dest(__dirname + "/ckanext/depositar_theme/fanstatic/styles/"));

const buildScss = () =>
  src(__dirname + "/ckanext/depositar_theme/fanstatic/scss/bootstrap-4.scss")
    .pipe(if_(with_sourcemaps(), sourcemaps.init()))
    .pipe(sass({ outputStyle: 'expanded' }).on('error', sass.logError))
    .pipe(if_(with_sourcemaps(), sourcemaps.write()))
    .pipe(dest(__dirname + "/ckanext/depositar_theme/fanstatic/styles/"));

const watchSource = () =>
  watch([
    __dirname + "/ckanext/depositar_theme/fanstatic/scss/**/*.scss",
    __dirname + "/ckanext/depositar_theme/fanstatic/less/**/*.less"],
    { ignoreInitial: false },
    parallel(
      buildLess,
      buildScss
    )
  );

const bootstrap = () =>
  src(__dirname + "/node_modules/bootstrap/scss/**/*").pipe(
    dest(__dirname + "/ckanext/depositar_theme/fanstatic/scss/vendor/bootstrap/")
  )

exports.build = parallel(
  buildLess,
  buildScss
);
exports.watch = watchSource;
exports.updateVendorLibs = parallel(
  bootstrap,
);
