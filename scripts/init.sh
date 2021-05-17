# exit on error
set -e


# try to create a virtual env with conda 
(conda create -y --prefix .venv pip) || \
    # if it fails, try using .venv
    (python3 -m venv .venv && . ./.venv/bin/activate && pip install --upgrade pip) || \
    # if it fails: warn the user (clean the .venv if it was partially created)
    (m -rf .venv && echo "ERROR: failed to create the .venv : do it yourself!" && exit 1);


echo "*********************************************************"
echo "Successfully created the virtual environment! it is located at:"
echo "$(pwd)/.venv"
echo "In order to activate this venv:"
echo "$ source scripts/activate.sh"
echo "*********************************************************"
echo ""