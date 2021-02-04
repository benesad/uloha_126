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


def breadth_first(graph):
    queue = []
    visited = []
    queue.append(graph.first_vertex)
    visited.append(graph.first_vertex)

    result = [[graph.first_vertex]]
    currentLevel = []

    while len(queue)!=0:
        vertex = queue.pop(0)
        if vertex in currentLevel:
            result.append(currentLevel)
            currentLevel = []
        
        for neighbour in vertex.neighbours:
            if neighbour not in visited:
                queue.append(neighbour)
                visited.append(neighbour)
                currentLevel.append(neighbour)

    return result


def save(file_name, tree):
    try:
        with open(file_name, "w", encoding="UTF-8") as physicFile:
            for level_index in range(len(tree)):
                row_str = ""

                for vertex in tree[level_index]:
                    if row_str=="":
                        row_str = str(vertex.label)
                    else:
                        row_str += " " + str(vertex.label)

                if level_index!=len(tree)-1:
                    row_str += '\n'
                    
                physicFile.write(row_str)


    except PermissionError:
        print(f"CHYBA: Nemuzu ulozit vysledny soubor, protoze nemam pristup k ukladani.")
        exit()
    except:
        print("CHYBA: Vysledny soubor se mi nepodarilo ulozit.")
        exit()


parser = argparse.ArgumentParser()
parser.add_argument('-i', '--input', required=False, default=None)
parser.add_argument('-o', '--output', required=False, default=None)
args = parser.parse_args()
if args.input != None and args.output != None:
    lines = read(args.input)
    result_tree = breadth_first(Graph(lines))
    save(args.output, result_tree)
else:
    print("Nezadali jste povinne argumenty (-i pro vstupni soubor, -o pro vystupni soubor.")
    exit()