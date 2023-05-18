from jinja2 import Template, Environment, FileSystemLoader

# Provide the actual values for the placeholders
data = {
    'instance_name': 'sabanatarajan',
    'region_name': ' us-central1',
    'zone': 'us-central1-a',
    'database_version': 'MYSQL_8_0',
    'instance_tier': 'db-f1-micro',
    'backup_enabled': 'true',
    'ipv4_enabled': 'true',
    'storage_auto_resize': 'true',
    'storage_size': 10,
    'storage_type': 'SSD',
    'environment': 'production',
    'root_password': 'my-root-password',
    'data_protection_enabled': 'true',
    'maintenance_hour': 2,
    'maintenance_day': 1
}

# Load the Jinja template file
env = Environment(loader=FileSystemLoader('.'))
template = env.get_template('mysql.yaml')

# Render the template with the provided data
rendered_yaml = template.render(data)

# Write the rendered YAML to a file
with open('mysql.yaml', 'w') as file:
    file.write(rendered_yaml)

# Print the rendered template
print(rendered_yaml)
