{%- extends 'basic.tpl' -%}
{% from 'mathjax.tpl' import mathjax %}

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

    {% else %}
        {{ super() }}
    {% endif %}
{%- endblock markdowncell %}

{% block footer %}
{% endblock footer %}
