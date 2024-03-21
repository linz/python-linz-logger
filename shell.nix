let
  pkgs = import (
    builtins.fetchTarball {
      name = "nixos-unstable-2024-06-05";
      url = "https://github.com/nixos/nixpkgs/archive/57610d2f8f0937f39dbd72251e9614b1561942d8.tar.gz";
      sha256 = "0k8az8vmfdk1n8xlza252sqk0hm1hfc7g67adin6jxqaab2s34n9";
    }
  ) {};
  poetry2nix =
    import (
      builtins.fetchTarball {
        name = "poetry2nix-2024.6.557458";
        url = "https://github.com/nix-community/poetry2nix/archive/81662ae1ad31491eae3bb1d976fb74c71853bc63.tar.gz";
        sha256 = "1zvlhzlc7mxr74qii3mkyn4iyd5rdivrm40yf7r7jvj9ry5gnbx9";
      }
    ) {
      inherit pkgs;
    };
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
      poetryPackages.poetryPackages
    ];
    shellHook = ''
      ln --force --no-target-directory --symbolic "${poetryPackages.python}/bin/python" python
    '';
  }
