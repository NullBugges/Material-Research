import pandas as pd
import requests
import json
import time

def translate_text(text, api_key):
    url = "https://api.siliconflow.cn/v1/chat/completions"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }
    
    payload = {
        "model": "deepseek-ai/DeepSeek-R1-Distill-Qwen-32B",
        "messages": [
            {
                "role": "system",
                "content": "你是一个专业的翻译助手，请将给定的英文文本翻译成中文。"
            },
            {
                "role": "user",
                "content": f"请将以下英文论文摘要翻译成中文并保留学术性（不要有任何的格式代码）：{text}"
            }
        ],
        "temperature": 0.7
    }

    try:
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()
        result = response.json()
        return result['choices'][0]['message']['content']
    except Exception as e:
        print(f"翻译出错: {str(e)}")
        return None

def main():
    # API密钥
    api_key = "API-key"
    
    try:
        # 读取Excel文件
        df = pd.read_excel('input.xlsx')
        
        # 创建新列用于存储翻译结果
        df['中文翻译'] = ''
        
        # 逐行翻译第2列的内容
        for index, row in df.iterrows():
            english_text = str(row.iloc[1])  # 获取第2列的文本
            if english_text and english_text.strip():
                translation = translate_text(english_text, api_key)
                if translation:
                    df.at[index, '中文翻译'] = translation
                    print(f"已翻译第 {index+1} 行")
                # 添加延时以避免API请求过于频繁
                time.sleep(1)
        
        # 保存结果到新的Excel文件
        df.to_excel('output.xlsx', index=False)
        print("翻译完成！结果已保存到 output.xlsx")
        
    except Exception as e:
        print(f"程序执行出错: {str(e)}")

if __name__ == "__main__":
    main()

def extract_innovation_points(text, api_key):
    url = "https://api.siliconflow.cn/v1/chat/completions"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }
    
    payload = {
        "model": "deepseek-ai/DeepSeek-R1-Distill-Qwen-32B",
        "messages": [
            {
                "role": "system",
                "content": "你是一个专业的学术研究助手，擅长从论文摘要中提炼核心创新点。"
            },
            {
                "role": "user",
                "content": f"请从以下论文中文摘要中提炼核心创新点，以简洁的要点形式列出（不要有任何的格式代码）：\n\n{text}"
            }
        ],
        "temperature": 0.7
    }

    try:
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()
        result = response.json()
        return result['choices'][0]['message']['content']
    except Exception as e:
        print(f"提炼创新点出错: {str(e)}")
        return None

def main():
    # API密钥
    api_key = "sk-yuttdrfyraahluyckvdjrysraciraealzamicrxjltifkfer"
    
    try:
        # 读取已翻译的Excel文件
        df = pd.read_excel('output.xlsx')
        
        # 创建新列用于存储创新点
        df['核心创新点'] = ''
        
        # 逐行提炼第3列(中文翻译)的创新点
        for index, row in df.iterrows():
            chinese_text = str(row['中文翻译'])  # 获取中文翻译列的文本
            if chinese_text and chinese_text.strip():
                innovation_points = extract_innovation_points(chinese_text, api_key)
                if innovation_points:
                    df.at[index, '核心创新点'] = innovation_points
                    print(f"已提炼第 {index+1} 行的创新点")
                # 添加延时以避免API请求过于频繁
                time.sleep(1)
        
        # 保存结果到新的Excel文件
        df.to_excel('output_with_innovations.xlsx', index=False)
        print("创新点提炼完成！结果已保存到 output_with_innovations.xlsx")
        
    except Exception as e:
        print(f"程序执行出错: {str(e)}")

if __name__ == "__main__":
    main()