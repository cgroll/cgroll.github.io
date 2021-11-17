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

### Adding Jupyter notebooks with leaflet maps

Currently leaflet maps are not displayed on github pages when the notebook is just rendered with the latest package versions. In order to fix this, the leaflet maps need to be rendered with a particular package version for "branca": 0.3.1 (see earth-gis repo). Hence:

- set branca to the correct version in the virtual environment of the notebook project
- render the notebook with the correct branca version activated
- convert the notebook to html
- add the html file to the github pages repo

# TODOs

- include sitemap to make page searchable
- site statistics (Google Analytics)
- add citations
- extend icons for easy sharing (LinkedIn)

# Further topics

- leveraged ETFs: synthetic creation, simulating payoffs
- time series momentum:
	- single time series strategy
	- multiple assets strategy
- Markowitz deficiencies
- diversification-aware frontier
- synthetic time series:
	- hedged time series
	- bond index prices
- financial market empiricism: return triangle, maximum drawdowns
- risk measures: max drawdown, dorfleitner
- benefits of diversification
- index tracking
- tracking error
- factor indices
- active vs passive (risk-adjusted returns)
- fallacies of time-varying dependence measures