import argparse
import subprocess
import os

def get_git_diff():
    """獲取當前 Git 專案的變更內容 (diff)。"""
    try:
        result = subprocess.run(['git', 'diff'], capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        print(f"Error getting git diff: {e}")
        return None

def generate_commit_message_ai(diff_content):
    """模擬 AI 生成 Commit Message。"""
    if not diff_content:
        return ["feat: Initial commit", "docs: Add README.md"]

    # In a real scenario, this would call an OpenAI API
    # For now, we'll return some mock suggestions based on diff presence
    suggestions = [
        "feat: Implement core AI commit message generation logic",
        "refactor: Improve git diff parsing and error handling",
        "docs: Update usage instructions in README",
        "chore: Add basic project structure and dependencies"
    ]
    return suggestions

def main():
    parser = argparse.ArgumentParser(description='AI-powered Git Commit Message Generator.')
    parser.add_argument('action', choices=['generate'], help='Action to perform (e.g., generate commit message).')

    args = parser.parse_args()

    if args.action == 'generate':
        print("Analyzing git changes...")
        diff = get_git_diff()

        if diff:
            print("\nDetected changes. Generating AI-powered commit message suggestions...")
        else:
            print("\nNo changes detected. Generating initial commit message suggestions.")

        suggestions = generate_commit_message_ai(diff)

        print("\n--- AI Commit Message Suggestions ---")
        for i, msg in enumerate(suggestions):
            print(f"{i+1}. {msg}")
        print("-------------------------------------")

        while True:
            try:
                choice = input("\nEnter the number of your preferred message, or type a custom message: ")
                if choice.isdigit() and 1 <= int(choice) <= len(suggestions):
                    selected_message = suggestions[int(choice) - 1]
                    break
                elif choice:
                    selected_message = choice
                    break
                else:
                    print("Invalid input. Please try again.")
            except ValueError:
                print("Invalid input. Please enter a number or a custom message.")

        print(f"\nSelected message: '{selected_message}'")
        confirm = input("Confirm commit? (y/n): ").lower()

        if confirm == 'y':
            try:
                subprocess.run(['git', 'commit', '-m', selected_message], check=True)
                print("Commit successful!")
            except subprocess.CalledProcessError as e:
                print(f"Error during git commit: {e}")
        else:
            print("Commit cancelled.")

if __name__ == '__main__':
    main()
