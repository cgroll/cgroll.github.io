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