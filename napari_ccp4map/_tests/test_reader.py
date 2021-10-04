from napari_ccp4map import napari_get_reader
from pathlib import Path

def test_reader(tmp_path):
    ccp4_file = Path(__file__).parent / "5wkd.ccp4"

    # try to read it back in
    reader = napari_get_reader(ccp4_file)
    assert reader is not None
    assert callable(reader)

    # make sure we're delivering the right format
    layer_data_list = reader(ccp4_file)
    assert isinstance(layer_data_list, list) and len(layer_data_list) > 0
    layer_data_arr = layer_data_list[0]
    assert isinstance(layer_data_arr, np.array) and len(layer_data_arr) > 0

def test_get_reader_pass():
    reader = napari_get_reader("fake.file")
    assert reader is None
