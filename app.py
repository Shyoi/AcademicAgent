import os
import streamlit as st
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, Settings, PromptTemplate
from llama_index.llms.openai import OpenAI

# ==========================================
# 页面基础配置
# ==========================================
st.set_page_config(page_title="AI学术裁缝 | 模块裁剪与重组系统", page_icon="✂️", layout="wide")

# 初始化 LLM (请确保环境变量中已配置 OPENAI_API_KEY，或在此处硬编码传递 api_key="...")
# os.environ["OPENAI_API_KEY"] = "your_api_key_here"
@st.cache_resource
def init_llm():
    return OpenAI(model="gpt-4o-mini", temperature=0.1)

Settings.llm = init_llm()

# ==========================================
# 后端 Agent 逻辑 (优化适配前端)
# ==========================================
class AcademicTailorSystem:
    def __init__(self, data_dir="./uploaded_papers"):
        self.data_dir = data_dir
        if not os.path.exists(self.data_dir):
            os.makedirs(self.data_dir)
        self.index = None

    def build_index(self):
        """ Agent 1: 检索 Agent (构建知识库) """
        documents = SimpleDirectoryReader(self.data_dir).load_data()
        if not documents:
            return False
        self.index = VectorStoreIndex.from_documents(documents)
        return True

    def run_reasoning_agent(self, query):
        """ Agent 2: 推理 Agent """
        if not self.index:
            return "推理失败：请先上传文献并构建知识库。"

        query_engine = self.index.as_query_engine(similarity_top_k=5, response_mode="compact")
        reasoning_prompt = PromptTemplate(
            "你是一个顶尖的计算机视觉与深度学习研究员。请基于以下文献内容，解答用户的重组构想。\n"
            "你的任务重点：\n"
            "1. 精准提取文献中提到的核心网络架构细节。\n"
            "2. 精准提取关键损失函数的数学或逻辑定义。\n"
            "3. 严谨评估用户提出的“模块拼接”方案的工程与理论可行性。\n"
            "---------------------\n"
            "文献上下文:\n{context_str}\n"
            "---------------------\n"
            "用户构想: {query_str}\n"
            "深度推理分析结果："
        )
        query_engine.update_prompts({"response_synthesizer:text_qa_template": reasoning_prompt})
        return query_engine.query(query)

    def run_synthesis_agent(self, reasoning_result):
        """ Agent 3: 综合 Agent """
        synthesis_prompt = PromptTemplate(
            "请将以下初步的算法模块推理分析结果，重新组织为一份排版精美的《算法模块裁剪与重组可行性报告》。\n"
            "必须包含：\n"
            "一、 核心目标场景\n"
            "二、 核心模块拆解 (详细列出网络子结构与损失函数)\n"
            "三、 跨模块融合可行性评估\n"
            "四、 研发建议\n"
            "---------------------\n"
            "初步推理素材：\n{reasoning_result}\n"
            "---------------------\n"
            "请直接输出 Markdown 格式的正式报告："
        )
        response = Settings.llm.complete(synthesis_prompt.format(reasoning_result=reasoning_result))
        return response.text

# 实例化系统
system = AcademicTailorSystem()

# ==========================================
# 前端 UI 布局
# ==========================================
st.title("✂️ 学术文献深度解析与算法模块裁剪系统")
st.markdown("基于多 Agent 协同与长链推理，快速评估跨文献算法模块“即插即用”的可行性。")

# 侧边栏：文件上传与知识库管理
with st.sidebar:
    st.header("📄 1. 文献知识库构建")
    uploaded_files = st.file_uploader("上传目标论文 (PDF格式)", type="pdf", accept_multiple_files=True)
    
    if st.button("🚀 构建/更新知识库", type="primary"):
        if uploaded_files:
            with st.spinner("正在解析 PDF 并构建向量空间..."):
                # 将上传的文件写入本地目录
                for file in uploaded_files:
                    file_path = os.path.join(system.data_dir, file.name)
                    with open(file_path, "wb") as f:
                        f.write(file.getbuffer())
                
                # 触发检索 Agent
                success = system.build_index()
                if success:
                    st.success(f"成功构建知识库！共录入 {len(uploaded_files)} 篇文献。")
                else:
                    st.error("知识库构建失败，请检查文件格式。")
        else:
            st.warning("请先上传至少一篇 PDF 文献。")

# 主界面：交互式查询
st.header("🧠 2. 模块重组构想验证")
default_query = (
    "针对夜间场景的红外与可见光图像融合任务，请评估一种‘先特征提取再融合’的重组方案："
    "保留 PIAFusion 中的光照感知子网络及其光照感知损失；"
    "同时，仅提取 Swin Transformer 的基础组成单元（一个窗口注意力机制block和移位窗口机制block）作为主干。"
    "分析该缝合方式在处理夜间光照不均和纹理丢失问题上的优势。"
)

query = st.text_area("输入你的学术裁剪构想 (描述你需要拼接哪些论文的哪个具体模块)：", value=default_query, height=150)

if st.button("⚡ 开始多 Agent 深度推理"):
    if not query.strip():
        st.warning("请输入具体的构想。")
    else:
        # 使用 st.status 增加极客感和执行过程的可视化
        with st.status("执行多 Agent 协同工作流...", expanded=True) as status:
            st.write("🕵️ [检索 Agent] 正在从知识库中召回相关模型结构与公式片段...")
            # 确保知识库已加载（如果是重启页面但本地已有文件）
            if not system.index:
                 system.build_index()
            
            st.write("🧠 [推理 Agent] 正在进行跨文档逻辑链比对与冲突检测...")
            raw_reasoning = system.run_reasoning_agent(query)
            
            st.write("📝 [综合 Agent] 正在汇总数据，生成结构化调研报告...")
            final_report = system.run_synthesis_agent(raw_reasoning)
            
            status.update(label="✅ 分析完成！", state="complete", expanded=False)

        st.divider()
        st.subheader("📑 调研与可行性报告")
        # 渲染最终 Markdown 结果
        st.markdown(final_report)