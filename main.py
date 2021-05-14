from pathlib import Path

import click

from measure.measure import count_sec
from measure.video import Video, Videos


@click.command()
@click.argument('video-files-dirname', type=click.Path(exists=True))
def main(video_files_dirname: str):
    videos_dir = Path(video_files_dirname)
    if not videos_dir.exists():
        raise click.BadParameter(f'{videos_dir} is not found')

    videos = Videos()
    for video_path in sorted(videos_dir.glob('*.mp4')):
        video = Video(video_path, count_sec(video_path))
        videos = videos.add(video)

    for video in videos:
        print(f'{video.viewing_time()}\t{video.path.name}')

    print('合計', videos.total_sec().to_mmss())


if __name__ == '__main__':
    main()
