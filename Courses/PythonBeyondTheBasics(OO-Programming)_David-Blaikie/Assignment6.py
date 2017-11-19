import os
import shutil

import pytest

from Assignment3 import ConfigDict
from Assignment4 import ConfigKeyError


class TestConfigDict:
    existing_fh = 'config_file.txt'
    existing_fh_template = 'config_file_template.txt'
    new_fh = 'config_file_new.txt'
    bad_path = '/some/bda/path/file.txt'

    def setup_class(self):
        shutil.copy(TestConfigDict.existing_fh_template, TestConfigDict.existing_fh)

    def teardown_class(self):
        os.remove(TestConfigDict.new_fh)

    def test_obj(self):
        cd = ConfigDict(TestConfigDict.existing_fh)
        assert isinstance(cd, ConfigDict)
        assert isinstance(cd, dict)

    def test_existing_filename(self):
        cd = ConfigDict(TestConfigDict.existing_fh)
        assert cd._config_file == TestConfigDict.existing_fh

    def test_new_filename(self):
        assert not os.path.isfile(TestConfigDict.new_fh)
        cd = ConfigDict(TestConfigDict.new_fh)
        assert cd._config_file == TestConfigDict.new_fh
        assert os.path.isfile(cd._config_file)

    def test_bad_filepath(self):
        with pytest.raises(IOError):
            ConfigDict(TestConfigDict.bad_path)

    def tet_read_dict(self):
        cd = ConfigDict(TestConfigDict.existing_fh)
        assert cd['a'] == '5'
        assert cd['b'] == '10'
        assert cd['c'] == 'this=that'

        with pytest.raises(ConfigKeyError):
            print(cd['x'])

    def test_write_dict(self):
        cd = ConfigDict(TestConfigDict.existing_fh)
        cd['zz'] = 'top'
        cd2 = ConfigDict(TestConfigDict.existing_fh)
        assert cd2['zz'] == 'top'
