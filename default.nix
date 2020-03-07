with import <nixpkgs> {};

let
  pyPkgs = python3Packages;
in pkgs.mkShell rec {
  name = "impurePythonEnv";
  venvDir = "./.venv";
  buildInputs = [
    pyPkgs.python
    pyPkgs.venvShellHook
    gcc
  ];
  postShellHook = ''
    pip install -r requirements.txt
'';
}
