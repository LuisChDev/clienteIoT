with import <nixpkgs> {};
mkShell {
  buildInputs = [
    python3
    mysql80
    redis
    # required to install pyls
    gcc
  ];
}
