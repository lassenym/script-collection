#!/bin/bash

# Check if yt-dlp is installed
if ! command -v yt-dlp &> /dev/null; then
    echo "yt-dlp is not installed. Please install it."
    exit 1
fi

# Function to play YouTube video in VLC
play_youtube() {
    # Fetch video URL
    video_url=$(yt-dlp -f bestvideo -g "$1")

    # Fetch audio URL
    audio_url=$(yt-dlp -f bestaudio -g "$1")

    # Check if yt-dlp command succeeded
    if [ $? -ne 0 ]; then
        echo "Failed to fetch YouTube audio or video URLs."
        exit 1
    fi

    # Play video in VLC with audio as input slave
    vlc "$video_url" --input-slave "$audio_url"
}

# Check if URL argument is provided
if [ -z "$1" ]; then
    echo "Usage: $0 <youtube_url>"
    exit 1
fi

# Call the function with the provided YouTube URL
play_youtube "$1"
