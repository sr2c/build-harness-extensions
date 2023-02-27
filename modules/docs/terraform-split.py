
LABEL_INPUTS = [
    "additional_tag_map",
    "attributes",
    "context",
    "delimiter",
    "enabled",
    "environment",
    "id_length_limit",
    "label_key_case",
    "label_order",
    "label_value_case",
    "labels_as_tags",
    "name",
    "namespace",
    "regex_replace_chars",
    "stage",
    "tags",
    "tenant"
]


def is_label_input(line):
    for pattern in [f"input_{input_name}" for input_name in LABEL_INPUTS]:
        if pattern in line:
            return True
    return False


with open("docs/terraform.md") as handle_docs:
    lines = handle_docs.readlines()
    inputs = []
    label_inputs = []
    while (line := lines.pop(0)) != "## Inputs\n":
        print(line.strip())
    lines.pop(0) # Remove blank line
    print("## Inputs")
    print()
    while (line := lines.pop(0)) != "\n":
        if is_label_input(line):
            label_inputs.append(line.strip())
        else:
            inputs.append(line.strip())
    for line in inputs:
        print(line)
    print()
    print("### Label Inputs")
    print()
    print("This Terraform module makes use of the [cloudposse/label/null](https://registry.terraform.io/modules/cloudposse/label/null/latest)")
    print("module to generate consistent names and tags for resources.")
    print("The label module contains many inputs that are common across all our modules that use the label module, and so")
    print("these inputs have been seperated here to make it clearer which inputs are specific to this module.")
    print()
    print("| Name | Description | Type | Default | Required |")
    print("|------|-------------|------|---------|:--------:|")
    for line in label_inputs:
        print(line)
    for line in lines:
        print(line.strip())