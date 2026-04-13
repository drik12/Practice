# Using JDK 21 in this workspace

This workspace includes a small helper script and a VS Code task to compile and run Java files using the locally installed JDK 21.

Files added:
- `run-java-21.sh` — sets `JAVA_HOME` to the JDK 21 install and compiles/runs a chosen main class (default `HelloWorld`).
- `.vscode/tasks.json` — VS Code task "Compile & Run with JDK 21" that executes the script.

Quick usage

From the project root you can run:

```bash
# run default HelloWorld
bash run-java-21.sh

# or specify a different main class
bash run-java-21.sh Exercise1
```

To run from VS Code:
1. Open the Command Palette (⇧⌘P) and choose "Tasks: Run Task".
2. Select "Compile & Run with JDK 21" and enter the main class when prompted (default `HelloWorld`).

Persisting JAVA_HOME in zsh

If you want Java 21 to be your default in all terminals and in VS Code, add the following to your `~/.zshrc` or `~/.zprofile`:

```bash
export JAVA_HOME="/Users/digantaroydrik/.jdk/jdk-21.0.8/jdk-21.0.8+9/Contents/Home"
export PATH="$JAVA_HOME/bin:$PATH"
```

Then reload your shell:

```bash
source ~/.zshrc
# or
source ~/.zprofile
```

If you'd like, I can automatically append those lines to your `~/.zshrc` for you — tell me and I'll do it (I will show the exact changes first).
