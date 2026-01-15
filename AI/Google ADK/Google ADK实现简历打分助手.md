## 代码
```
import os

from google.adk.agents import SequentialAgent
from google.adk.agents.llm_agent import Agent
from google.adk.models import LiteLlm

os.environ["OPENAI_API_BASE"] = "api地址"
os.environ["OPENAI_API_KEY"] = "sk-xxx"

resume_convert = Agent(
    name='resume_convert',
    model=LiteLlm(
        model="openai/deepseek-v3.1",
    ),
    description='将简历信息转换成json',
    instruction="""
    你是一个专业的简历信息提取助手。请从提供的简历文本中准确提取以下五个字段的信息：

    姓名（name）
    年龄（age）
    工作年限（work_years）
    学历（education）
    技术栈（tech_stack）
    要求如下：

    姓名：提取候选人的真实中文或英文全名。
    年龄：若简历中未直接提供年龄，请根据出生年份推算（当前年份为 2026 年）；若无法推算，则填写 null。
    工作年限：提取明确说明的工作年限（如“5年工作经验”），或根据工作经历时间段估算总年限（四舍五入取整）；若无法确定，填写 null。
    学历：提取最高学历，如"大专","专科",“本科”、“硕士”、“博士”等；其中大专和专科都以专科为结果，若学历未提及，填写 null。
    技术栈：提取简历中提到的所有技术、编程语言、框架、工具等，整理为一个字符串数组；若未提及技术相关内容，返回空数组 []。
    请将结果以标准 JSON 格式输出，不要包含任何额外说明、注释或 Markdown 语法。字段名使用英文小写加下划线，严格按上述顺序。
    `
    {   
      "name": "张三",
      "age": 28,
      "work_years": 5,
      "education": "本科",
      "tech_stack": ["Python", "Django", "MySQL", "Docker"]
    }
    `
    """,
    output_key="resume"
)

score_agent = Agent(
    name='score_agent',
    model=LiteLlm(
        model="openai/deepseek-v3.1",
    ),
    description='对简历进行打分',
    instruction="""
    你是一个专业简历打分助手。请从下面提供的简历文本中，对简历进行打分。
    岗位要求如下：
        - 学历为本科
        - 熟悉mysql，postgres，redis等数据库
        - 熟练使用django、fastapi等python web开发框架

    打分标准如下：
    学历（Education）权重20:
        - 博士：20 分
        - 硕士（985/211 或全球 Top 100）：18 分
        - 硕士（普通院校）：15 分
        - 本科（985/211 或全球 Top 200）：16 分
        - 本科（普通院校）：12 分
        - 专科：8 分
        - 无学历或未注明：0–5 分（视情况）
    工作年限（Experience）权重30
        - ≥8 年：30 分
        - 6–7 年：26 分
        - 4–5 年：22 分
        - 2–3 年：16 分
        - 1 年：10 分
        - <1 年 或 应届生：5 分
        - 无明确信息：0 分
    技术栈（Tech Stack）权重50
        根据 相关性、深度、广度、主流性 综合评估：
        基础要求（岗位匹配）（20 分）
        
        - 完全匹配核心技能（符合岗位要求的技能及编程语言（编程语言有限））：20 分
        - 部分匹配：10–15 分
        - 不匹配：0–5 分
        
        技术广度与深度（20 分）
        - 掌握 ≥5 项主流技术（含框架/数据库/中间件/云服务等），且有项目体现：16–20 分
        - 掌握 3–4 项：10–15 分
        - ≤2 项或描述模糊：0–9 分
        
        前沿/高价值技术（10 分）
        - 包含如 Kubernetes、Kafka、Spark、LLM、TensorFlow、AWS/GCP 高级服务等：+5～10 分
        - 仅基础技术：+0～4 分
    )
    """,
    output_key="score"

)

result_agent = Agent(
    name='result_agent',
    model=LiteLlm(
        model="openai/deepseek-v3.1",
    ),
    description='简历推荐',
    instruction="""
    你将收到一个包含若干候选人信息的列表，每个候选人包括：
    name（姓名）
    score（总分，整数）
    summary（简历摘要）
    # 输出要求
        按 score 从高到低排序；
        推荐 得分最高的 3 到 5 人（若总人数 ≤5，则全部推荐；若 >5，只取前 5）；
        为每位推荐候选人简要说明推荐理由（50 字以内），聚焦其核心优势（如“6年全栈经验 + 掌握 AWS”）；
        以 清晰的 JSON 格式 输出，包含字段：rank（排名）、name、score、reason；
        不要输出任何额外解释、标题或 Markdown。
    # 输出实例
    `
    [
      {
        "rank": 1,
        "name": "张伟",
        "score": 89,
        "reason": "985本科，6年全栈经验，技术栈覆盖前端、后端及云服务"
      },
      {
        "rank": 2,
        "name": "李娜",
        "score": 85,
        "reason": "硕士学历，5年后端开发，精通 Java 生态与 Kafka"
      }
    ]
    `
    """
)

code_pipeline_agent = SequentialAgent(
    name="CodePipelineAgent",
    sub_agents=[resume_convert, score_agent, result_agent],
    description="执行一个读取简历，抽取简历关键信息，简历打分，候选人推荐流程",
    # The agents will run in the order provided: Writer -> Reviewer -> Refactorer
)

root_agent = code_pipeline_agent
```
## 效果
![](https://jruing-blogs.oss-cn-beijing.aliyuncs.com/blogs/微信图片_20260107190744_37_4.png)
![](https://jruing-blogs.oss-cn-beijing.aliyuncs.com/blogs/微信图片_20260107190744_38_4.png)