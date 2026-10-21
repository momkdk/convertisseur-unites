"""CLI : python -m convertisseur_unites <categorie> <valeur> <unite_depart> <unite_arrivee>"""

from __future__ import annotations

import argparse
import sys

from . import __version__
from .conversion import CATEGORIES, convertir, convertir_temperature


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(prog="convertisseur_unites", description=__doc__)
    p.add_argument("--version", action="version", version=__version__)
    p.add_argument("categorie", choices=[*CATEGORIES, "temperature"])
    p.add_argument("valeur", type=float)
    p.add_argument("unite_depart")
    p.add_argument("unite_arrivee")
    args = p.parse_args(argv)

    try:
        if args.categorie == "temperature":
            resultat = convertir_temperature(args.valeur, args.unite_depart, args.unite_arrivee)
        else:
            resultat = convertir(args.valeur, args.unite_depart, args.unite_arrivee, args.categorie)
    except ValueError as e:
        print(f"Erreur : {e}", file=sys.stderr)
        return 1

    print(f"{args.valeur} {args.unite_depart} = {resultat:.6g} {args.unite_arrivee}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
