import argparse
from graph import Graph

def read(input_name):
        try:
            with open(input_name, "r", encoding="UTF-8") as physicFile:
                return physicFile.read().splitlines()
        except FileNotFoundError: # zjistuje, zda existuje
            print(f"CHYBA: Pozadovany soubor {input_name} neexistuje. Program skonci.")
            exit()
        except PermissionError: # zjistuje pristup k souboru
            print(f"CHYBA: Nemam pristup k {input_name}.Program skonci.")
            exit()
        except ValueError as e: # validuje i pokud se jedna o validni JSON
            print(f"CHYBA: Soubor {input_name} neni validni. Program skonci.\n", e)
            exit()


parser = argparse.ArgumentParser()
parser.add_argument('-i', '--input', required=False, default=None)
parser.add_argument('-o', '--output', required=False, default=None)
args = parser.parse_args()
if args.input != None and args.output != None:
    lines = read(args.input)
    G = Graph(lines)
else:
    print("Nezadali jste povinne argumenty (-i pro vstupni soubor, -o pro vystupni soubor.")
    exit()