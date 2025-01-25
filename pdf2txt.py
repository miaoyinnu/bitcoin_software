#!/usr/bin/env python3
import argparse
import os
from PyPDF2 import PdfReader

def pdf_to_txt(pdf_path, output_path=None):
    """
    将PDF文件转换为TXT文件
    :param pdf_path: PDF文件路径
    :param output_path: 输出TXT文件路径（可选）
    :return: None
    """
    try:
        # 如果未指定输出路径，使用原文件名（更改扩展名为.txt）
        if output_path is None:
            output_path = os.path.splitext(pdf_path)[0] + '.txt'
        
        # 打开PDF文件
        reader = PdfReader(pdf_path)
        
        # 提取文本
        with open(output_path, 'w', encoding='utf-8') as txt_file:
            for page in reader.pages:
                text = page.extract_text()
                txt_file.write(text + '\n')
                
        print(f'转换成功！输出文件：{output_path}')
        
    except Exception as e:
        print(f'转换失败：{str(e)}')

def main():
    # 创建命令行参数解析器
    parser = argparse.ArgumentParser(description='将PDF文件转换为TXT文件')
    parser.add_argument('pdf_path', help='PDF文件路径')
    parser.add_argument('-o', '--output', help='输出TXT文件路径（可选）')
    
    # 解析命令行参数
    args = parser.parse_args()
    
    # 执行转换
    pdf_to_txt(args.pdf_path, args.output)

if __name__ == '__main__':
    main() 