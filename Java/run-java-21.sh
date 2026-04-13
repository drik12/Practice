#!/usr/bin/env bash
set -euo pipefail
# Workspace helper script: set JAVA_HOME to the locally installed JDK 21 and run a Java class.
# Usage: ./run-java-21.sh [MainClass]

WORKSPACE_DIR="$(cd "$(dirname "$0")" && pwd)"

# Update this path if your JDK 21 install is in a different location.
JAVA_HOME="/Users/digantaroydrik/.jdk/jdk-21.0.8/jdk-21.0.8+9/Contents/Home"
export JAVA_HOME
export PATH="$JAVA_HOME/bin:$PATH"

OUT_DIR="$WORKSPACE_DIR/out"
mkdir -p "$OUT_DIR"

MAIN_CLASS="${1:-HelloWorld}"

echo "Using JAVA_HOME=$JAVA_HOME"
echo "Compiling all .java files in $WORKSPACE_DIR to $OUT_DIR..."
javac "$WORKSPACE_DIR"/*.java -d "$OUT_DIR"

echo "Running main class: $MAIN_CLASS"
java -cp "$OUT_DIR" "$MAIN_CLASS"
