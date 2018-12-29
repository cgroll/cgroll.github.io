# Set up environment

Install Jekyll:

```
gem install jekyll
gem install jekyll bundler
```

Run local server:

```
bundle exec jekyll serve
```

# Instructions

## Adding / posting Jupyter notebooks

- export / convert .ipynb notebook to html without headers:

```
jupyter nbconvert --to html --template basic
```

- add .html file to ./_includes/notebooks/
- create new blog post and include .html file similar to:

```
{% include notebooks/tut_german_interest_rates_and_bond_indices.html %}
```

# TODOs

- include sitemap to make page searchable
- site statistics (Google Analytics)
- add citations
- extend icons for easy sharing (LinkedIn)
