from jinja2 import Template, Environment, FileSystemLoader

# Provide the actual values for the placeholders
data = {
    'name': 'saba',
    'zone': 'us-central1-a',
    'size': 10,
    'value': 'pd-standard',
    'deletion_protection_enabled': 'true',
    'physical_block_sixe_byte': '4096'
}

# Load the Jinja template file
env = Environment(loader=FileSystemLoader('.'))
template = env.get_template('persistent-disk.yaml')

# Render the template with the provided data
rendered_yaml = template.render(data)

# Write the rendered YAML to a file
with open('persistent-disk.yaml', 'w') as file:
    file.write(rendered_yaml)

# Print the rendered template
print(rendered_yaml)
