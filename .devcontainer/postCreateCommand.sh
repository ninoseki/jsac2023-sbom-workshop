#!/bin/bash

echo "Setting up the lab env..."


# setup Poetry
cd /workspaces/jsac2023-sbom-workshop

echo "Install Poetry..."
pip install --user -r requirements.txt --quiet

poetry config virtualenvs.in-project true --local

echo "Install dependencies by Poetry..."
poetry install --no-ansi -q -n

echo "Done! You are ready for the workshop."
