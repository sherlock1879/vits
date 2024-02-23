import os

def process_file(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as infile:
        lines = infile.readlines()

    filtered_lines = []

    for line in lines:
        parts = line.strip().split('|')
        if len(parts) >= 2:
            relative_path = parts[0]
            full_path = f"D:/workspace/bishe/vits/{relative_path}"
            if os.path.exists(full_path):
                filtered_lines.append(line.strip())
            else:
                print(f"File not found: {full_path}. Removing line: {line.strip()}")

    with open(output_file, 'w', encoding='utf-8') as outfile:
        outfile.write('\n'.join(filtered_lines))

if __name__ == "__main__":
    input_file_path = "D:\\workspace\\bishe\\vits\\filelists\\vctk_audio_sid_text_val_filelist.txt.cleaned"  # 替换为你的输入文件路径
    output_file_path = "D:\\workspace\\bishe\\vits\\filelists\\output.txt"  # 替换为你的输出文件路径

    process_file(input_file_path, output_file_path)
