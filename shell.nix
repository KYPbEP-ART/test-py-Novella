{ pkgs ? import <nixpkgs> {} }:

pkgs.mkShell {
  name = "prak12-migration";

  packages = [
    (pkgs.python3.withPackages (python-pkgs: with python-pkgs; [
      fastapi
      uvicorn
      sqlalchemy
      # добавляй сюда другие библиотеки
    ]))
  ];

  shellHook = ''
    python --version
    echo "Запуск: python main.py"
  '';
}