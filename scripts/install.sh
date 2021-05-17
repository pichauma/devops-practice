
echo "Installing packages from $1"
(conda install --file "$1") || \
    # if it fails, try to activate with ".venv""
    (pip install -r "$1") || \
    # if it fails: warn the user and exit
    ( echo ""; echo "ERROR: failed to install do it manually"; return 1 )
