# Video Frame Extractor

A Python script that extracts frames from video files with customizable settings. Extract high-quality still images from your videos with precise control over output parameters.

## Features

- Support for multiple video formats (.mp4, .avi, .mov, .mkv)
- Customizable frame extraction rate
- Automatic image resizing
- Configurable JPEG quality
- Organized output directory structure
- Date-stamped frame naming

## Installation

1. Ensure you have Python 3.x installed on your system
2. Install the required dependencies:

```bash
pip install opencv-python numpy
```

## Usage

1. Run the script:
```bash
python video_to_frames.py
```

2. Follow the interactive prompts:
   - Select your input video file
   - Enter a custom name for the output frames

## Configuration

Default settings are defined in `video_to_frames.py`:

| Setting | Default Value | Description |
|---------|--------------|-------------|
| FPS | 5 | Number of frames extracted per second |
| Resize | 50% | Output image size relative to source |
| JPEG Quality | 85% | Compression quality for saved images |

## Output Structure

Extracted frames are saved with the following organization:

```
image_data/
└── [custom_name]/
    ├── [custom_name]_[date]_001.jpg
    ├── [custom_name]_[date]_002.jpg
    └── ...
```

## Requirements

- Python 3.x
- OpenCV
- NumPy

## License

This project is open source and available under the MIT License.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
