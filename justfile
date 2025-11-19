set shell := ["bash", "-uc"]
set windows-shell := ["powershell.exe", "-NoLogo", "-Command"]

# List available recipes
default:
    @just --list

alias g := generate
# Copy template with Copier
generate input_dir="." output_dir="generated":
    copier copy --data-file example_data.yaml --trust --vcs-ref HEAD {{input_dir}} {{output_dir}}