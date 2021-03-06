{%- extends 'basic.tpl' -%}
{% from 'mathjax.tpl' import mathjax %}


{%- block header -%}
<!DOCTYPE html>
<html>
<head>
{%- block html_head -%}
<meta charset="utf-8" />
<title>Notebook Insights</title>

<script src="https://cdnjs.cloudflare.com/ajax/libs/require.js/2.1.10/require.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/2.0.3/jquery.min.js"></script>
<link rel="shortcut icon" href="/favicon.png" type="image/x-icon"/>


<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/jqueryui/1.12.1/jquery-ui.css">
<script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/jqueryui/1.9.1/jquery-ui.min.js"></script>
<link rel="stylesheet" type="text/css" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">

{% for css in resources.inlining.css -%}
    <style type="text/css">
    {{ css }}
    </style>
{% endfor %}

<style type="text/css">
/* Overrides of notebook CSS for static HTML export */
body {
  overflow: visible;
  padding: 8px;
}

div#notebook {
  overflow: visible;
  border-top: none;
}

.prompt{
	display: None;
}


@media print {
  div.cell {
    display: block;
    page-break-inside: avoid;
  } 
  div.output_wrapper { 
    display: block;
    page-break-inside: avoid; 
  }
  div.output { 
    display: block;
    page-break-inside: avoid; 
  }
}
</style>

<style>
/* Hide code cells by default. */
.hidden {
    display: none;
}
div.cell > :first-child {
    padding: 5px 0;
}
div.cell {
    padding: 0 5px;
    border-width: 0;
}

@media (min-width: 1400px) {
    .container {
        width: 1340px;
        padding: 40px 15px 50px 15px !important;
    }
}
#notebook-container {
    margin-bottom: 50px;
}
</style>

<!-- Loading mathjax macro -->
{{ mathjax() }}
{%- endblock html_head -%}
</head>
{%- endblock header -%}

{% block body %}
<body>
  <div tabindex="-1" id="notebook" class="border-box-sizing">
    <div class="container" id="notebook-container">

        {{ super() }}
    </div>
  </div>
</body>
{%- endblock body %}

{% block input_group -%}
    {% if 'nohide' in cell['metadata'].get('tags', []) %}
            {{ super() }}
    {% else %}
        <!-- Do nothing -->
    {% endif %}
{% endblock input_group %}

{% block output_group -%}
    {% if 'hide' in cell['metadata'].get('tags', []) or 'hide-output' in cell['metadata'].get('tags', []) %}
        <div class="hideable hidden">
            {{ super() }}
        </div>
    {% else %}
        {{ super() }}
    {% endif %}
{% endblock output_group %}

{% block markdowncell scoped %}
    {% if 'hide' in cell['metadata'].get('tags', []) %}
        <div class="hideable hidden">
            {{ super() }}
        </div>
    {% else %}
        {{ super() }}
    {% endif %}
{%- endblock markdowncell %}

{% block footer %}
</html>
{% endblock footer %}
