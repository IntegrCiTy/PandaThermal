import pytest
import pandathermal as pth


@pytest.fixture()
def fix_create():
    g = pth.create_empty_directed_network()

    pth.add_srce(g, "SRCE")

    pth.add_sink(g, "SNK1", p_kw=10.0)
    pth.add_sink(g, "SNK2", p_kw=20.0)
    pth.add_sink(g, "SNK3", p_kw=10.0)
    pth.add_sink(g, "SNK4", p_kw=50.0)
    pth.add_sink(g, "SNK5", p_kw=10.0)
    pth.add_sink(g, "SNK6", p_kw=20.0)
    pth.add_sink(g, "SNK7", p_kw=10.0)
    pth.add_sink(g, "SNK8", p_kw=30.0)
    pth.add_sink(g, "SNK9", p_kw=10.0)

    pth.add_nodes_from(g, ["N{}".format(i) for i in range(7)])

    edges = [
        ("SRCE", "N0"),
        ("N0", "SNK1"),
        ("N1", "SNK2"),
        ("N2", "SNK3"),
        ("N2", "SNK4"),
        ("N2", "SNK5"),
        ("N3", "SNK6"),
        ("N4", "SNK7"),
        ("N5", "SNK8"),
        ("N6", "SNK9"),
        ("N0", "N1"),
        ("N1", "N2"),
        ("N2", "N3"),
        ("N3", "N4"),
        ("N4", "N5"),
        ("N5", "N6"),
    ]
    pth.add_pipes_from(g, edges)

    return g


def test_compute_pipes_diameter(fix_create):
    g = fix_create
    waited = {
        ("SRCE", "N0"): 0.72,
        ("N0", "SNK1"): 0.17,
        ("N0", "N1"): 0.7,
        ("N1", "SNK2"): 0.25,
        ("N1", "N2"): 0.65,
        ("N2", "SNK3"): 0.17,
        ("N2", "SNK4"): 0.39,
        ("N2", "SNK5"): 0.17,
        ("N2", "N3"): 0.46,
        ("N3", "SNK6"): 0.25,
        ("N3", "N4"): 0.39,
        ("N4", "SNK7"): 0.17,
        ("N4", "N5"): 0.35,
        ("N5", "SNK8"): 0.3,
        ("N5", "N6"): 0.17,
        ("N6", "SNK9"): 0.17,
    }
    assert pth.compute_pipes_diameter(g, dt=40) == waited
