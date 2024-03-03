import networkx as nx
import matplotlib.pyplot as plt


def main_roads():
    roads = {("Lviv", "Rivne"): {"weight": 211}, ("Rivne", "Zhytomyr"): {"weight": 190},
             ("Zhytomyr", "Kyiv"): {"weight": 139}, ("Kyiv", "Uman"): {"weight": 211},
             ("Uman", "Odesa"): {"weight": 271}, ("Kyiv", "Poltava"): {"weight": 351},
             ("Poltava", "Kharkiv"): {"weight": 143}, ("Kharkiv", "Dnipro"): {"weight": 221},
             ("Dnipro", "Zaporizhzhya"): {"weight": 85}, ("Dnipro", "Kryvyi Rih"): {"weight": 146},
             ("Kryvyi Rih", "Mykolayiv"): {"weight": 182}, ("Mykolayiv", "Kherson"): {"weight": 68},
             ("Mykolayiv", "Odesa"): {"weight": 135}, ("Uman", "Vinnytsya"): {"weight": 160},
             ("Vinnytsya", "Khmelnytskyi"): {"weight": 121}, ("Khmelnytskyi", "Ternopil"): {"weight": 112},
             ("Ternopil", "Lviv"): {"weight": 128}
             }

    pos = {
        "Uman": (0, 0), "Kyiv": (0.2, 2), "Odesa": (0.2, -2), "Poltava": (3, 1.7), "Kharkiv": (4, 2),
        "Dnipro": (3.5, 0), "Kryvyi Rih": (2.2, -0.8), "Mykolayiv": (1.5, -1.8), "Kherson": (2, -1.9),
        "Zaporizhzhya": (3.8, -0.5), "Vinnytsya": (-1.5, 0.5), "Khmelnytskyi": (-3, 0.7), "Ternopil": (-4.5, 0.8),
        "Lviv": (-6, 1), "Rivne": (-4, 2), "Zhytomyr": (-1.6, 1.7)
    }

    options = {
        "node_color": "yellow",
        "edge_color": "blue",
        "node_size": 500,
        "width": 3,
        "with_labels": True,
    }

    G = nx.Graph()
    for edge, attributes in roads.items():
        G.add_edge(*edge, **attributes)

    nx.draw(G, pos, **options)
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
    plt.title("Main roads of Ukraine")
    plt.show()

    shortest_paths = nx.single_source_dijkstra_path(G, source='Lviv')
    shortest_path_lengths = nx.single_source_dijkstra_path_length(G, source='Lviv')

    print(shortest_paths)
    print(shortest_path_lengths)


if __name__ == '__main__':
    main_roads()
