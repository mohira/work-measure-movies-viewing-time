from pathlib import Path

import pytest

from measure.measure import count_sec, Sec


class Test動画時間を秒単位で計測できる:
    @pytest.fixture()
    def fixture_path(self) -> Path:
        return Path(__file__).parent / 'video_fixtures'

    def test_1(self, fixture_path: Path):
        sec = count_sec(fixture_path / 'sample1.mp4')
        assert sec == Sec(3)


class Test秒数をいい感じのフォーマットにできる:
    @pytest.mark.parametrize('seconds, expected', (
            (45, '00:45'),
            (60, '01:00'),
            (612, '10:12'),
            (72072, '20:01:12'),
    ))
    def test_1(self, seconds: int, expected: str):
        assert Sec(seconds).to_mmss() == expected
