let
  pkgs = import (builtins.fetchTarball {
    name = "nixos-unstable-2024-10-17";
    url = "https://github.com/nixos/nixpkgs/archive/a3c0b3b21515f74fd2665903d4ce6bc4dc81c77c.tar.gz";
    sha256 = "1wn29537l343lb0id0byk0699fj0k07m1n2d7jx2n0ssax55vhwy";
  }) { };
  poetry2nix = import (builtins.fetchTarball {
    url = "https://github.com/nix-community/poetry2nix/archive/2024.10.1637698.tar.gz";
    sha256 = "08w14qxgn6rklfc83p8z6h91si854kl6nr1pjhdn8smfx7nw5819";
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
