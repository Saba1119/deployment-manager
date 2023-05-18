from jinja2 import Template, Environment, FileSystemLoader

# Provide the actual values for the placeholders
data = {
    'project_id': 'develop-375210',
    'bucket_name': 'saab123',
    'bucket_location': 'us-east1',
    'storage_class': 'COLDLINE',
    'deletion_age': 60
}

# Load the Jinja template file
env = Environment(loader=FileSystemLoader('.'))
template = env.get_template('storage-bucket.yaml')

# Render the template with the provided data
rendered_yaml = template.render(data)

# Write the rendered YAML to a file
with open('storage-bucket.yaml', 'w') as file:
    file.write(rendered_yaml)

# Print the rendered template
print(rendered_yaml)
