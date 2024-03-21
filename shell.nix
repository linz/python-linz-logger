let
  pkgs = import (builtins.fetchTarball {
    name = "nixos-unstable-2024-09-17";
    url = "https://github.com/nixos/nixpkgs/archive/345c263f2f53a3710abe117f28a5cb86d0ba4059.tar.gz";
    sha256 = "1llzyzw7a0jqdn7p3px0sqa35jg24v5pklwxdybwbmbyr2q8cf5j";
  }) { };
  poetry2nix = import (builtins.fetchTarball {
    url = "https://github.com/nix-community/poetry2nix/archive/2024.9.1542864.tar.gz";
    sha256 = "06vz5hwylvjvx4ywbv4y3kadq8zxmvpf5h7pjy6w1yhkwpjd6k25";
  }) { inherit pkgs; };
  poetryPackages = poetry2nix.mkPoetryPackages {
    projectDir = builtins.path {
      path = ./.;
      name = "python-linz-logger";
    };
  };
in
pkgs.mkShell {
  packages = [
    pkgs.bashInteractive
    pkgs.poetry
    pkgs.deadnix
    pkgs.gitFull
    pkgs.nixfmt-rfc-style
    pkgs.statix
    poetryPackages.poetryPackages
    poetryPackages.python.pkgs.pip # For IDEA package resolution
    poetryPackages.python.pkgs.setuptools # For IDEA package resolution
  ];
  shellHook = ''
    ln --force --no-target-directory --symbolic "${poetryPackages.python}/bin/python" python
  '';
}
