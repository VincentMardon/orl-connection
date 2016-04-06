# Require any additionnal compass plugins here.
# ---------------------------------------------

require 'sass-globbing'


# Configure folders.
# ------------------

sass_dir        = 'static/sass'
css_dir         = 'static/assets/css'
images_dir      = 'static/assets/img'
fonts_dir       = 'static/assets/fonts'
javascripts_dir = 'static/assets/js'
relative_assets = true


# Enable sourcemaps on everything but not production.
# ---------------------------------------------------

sourcemap = (environment == :production) ? false : true


# Configuration wether environment.
# ---------------------------------

if environment == :production
  output_style = :compressed
else
  output_style = :expanded
  sass_options = { :debug_info => true }
end