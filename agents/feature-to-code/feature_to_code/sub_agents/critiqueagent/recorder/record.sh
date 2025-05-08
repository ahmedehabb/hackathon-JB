#!/bin/bash
export DISPLAY=:0

# 1. Start server in the background
cd new_project
npx http-server -p 3000 > /dev/null 2>&1 &
SERVER_PID=$!
cd ..

# 2. Wait for the server to be ready
echo "⏳ Waiting for the server to be ready..."
while ! nc -z localhost 3000; do
  sleep 0.5  # Retry every 0.5 seconds
done
echo "✅ Server is ready!"

# 3. Open Chromium via the interaction script
echo "🚀 Launching Chromium with record_interaction.js..."
node record_interaction.js &  # Run the script in the background
INTERACTION_PID=$!

# 4. Wait for Chromium to initialize (optional: tweak logic as needed)
sleep 0.6  # Wait for half a seconds to give Chromium time to load properly

# 5. Start recording screen (1280x720 at top-left) in background
echo "🎥 Starting screen recording..."
ffmpeg -y -f avfoundation -framerate 30 -t 10 -video_size 1280x720 -i "Capture screen 0" output.mp4 > /dev/null 2>&1 &
FFMPEG_PID=$!

# 6. Wait for recording to finish
wait $FFMPEG_PID

# 7. Kill the server
kill $SERVER_PID

# # 8. Kill interaction script if needed
kill $INTERACTION_PID 2>/dev/null

# 9. Output result
echo "🎬 Recording saved as output.mp4"

