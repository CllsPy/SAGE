import streamlit as st
import PyPDF2
from sumarizer.main import initialize_model, summarize
import time
from st_copy_to_clipboard import st_copy_to_clipboard
import os

# Configuração da página
st.set_page_config(
    page_title='Paper Summarizer',
    layout='wide',
    initial_sidebar_state='collapsed',
)

# Estilos CSS aprimorados usando princípios de design
st.markdown("""
    <style>
    /* Typography System */
    h1, h2, h3, h4, h5, h6 {
        color: #1A1F36;
        font-family: 'sans-serif';
        letter-spacing: -0.02em;
    }
    
    /* Card Styles */
    .card {
        background: white;
        border-radius: 12px;
        padding: 1.5rem;
        box-shadow: 0 2px 4px rgba(45, 104, 255, 0.1);
        border: 1px solid rgba(45, 104, 255, 0.1);
        margin: 1rem 0;
    }
    
    /* Button Styles */
    .stButton>button {
        height: 3rem;
        background: linear-gradient(135deg, #2D68FF 0%, #1A54FF 100%);
        color: white;
        border-radius: 8px;
        font-weight: 600;
        font-size: 1rem;
        border: none;
        transition: transform 0.2s ease;
    }
    
    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 12px rgba(45, 104, 255, 0.2);
    }
    
    /* Upload Box */
    .upload-box {
        border: 2px dashed #2D68FF;
        border-radius: 12px;
        padding: 2rem;
        text-align: center;
        background: #F5F8FF;
        transition: all 0.3s ease;
    }
    
    .upload-box:hover {
        background: #EDF1FF;
        border-color: #1A54FF;
    }
    
    /* Headers */
    .big-font {
        font-size: 2.5rem !important;
        font-weight: 800;
        background: linear-gradient(135deg, #2D68FF 0%, #1A54FF 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 1rem;
    }
    
    /* Success Messages */
    .success-box {
        background: #E6F7EE;
        border: 1px solid #00B37E;
        color: #00B37E;
        padding: 1rem;
        border-radius: 8px;
        margin: 1rem 0;
    }
    
    /* Custom Spacing */
    .section-spacing {
        margin: 2rem 0;
    }
    
    /* Sidebar styling */
    .css-1d391kg {
        background: #F5F8FF;
    }
    
    /* Results area */
    .results-container {
        background: white;
        border-radius: 12px;
        padding: 2rem;
        margin-top: 2rem;
        border: 1px solid rgba(45, 104, 255, 0.1);
    }
    </style>
    """, unsafe_allow_html=True)

def read_sample_pdf():
    sample_path = os.path.join('assets', 'pdf/Rosenblatt1958.pdf')
    if os.path.exists(sample_path):
        with open(sample_path, 'rb') as file:
            pdf_reader = PyPDF2.PdfReader(file)
            text_content = ""
            for page in pdf_reader.pages:
                text_content += page.extract_text()
            return text_content
    return None

# Layout principal
st.markdown('<div style="padding: 2rem 0;">', unsafe_allow_html=True)
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.markdown('<p class="big-font" style="text-align: center;">Paper Summarizer AI</p>', unsafe_allow_html=True)
    st.markdown(
        '<p style="text-align: center; color: #1A1F36; font-size: 1.2rem;">'
        'Transforme artigos científicos em resumos estruturados usando IA'
        '</p>', 
        unsafe_allow_html=True
    )

# Container principal
main_container = st.container()
with main_container:
    left_col, center_col, right_col = st.columns([1, 2, 1])
    
    with center_col:
        # Seção de API
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown(
            '<h3 style="color: #1A1F36; margin-bottom: 1rem;">⚙️ Configuração</h3>',
            unsafe_allow_html=True
        )
        api_key = st.text_input(
            "Chave API do Google",
            type="password",
            help="Insira sua chave API do Google para usar o serviço"
        )
        st.markdown('</div>', unsafe_allow_html=True)

        # Seção de upload
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown(
            '<h3 style="color: #1A1F36; margin-bottom: 1rem;">📎 Selecione o Documento</h3>',
            unsafe_allow_html=True
        )
        
        use_sample = st.checkbox(
            "💡 Usar artigo de exemplo (Rosenblatt, 1958)",
            value=False
        )
        
        if not use_sample:
            st.markdown('<div class="upload-box">', unsafe_allow_html=True)
            uploaded_file = st.file_uploader(
                "Arraste e solte seu PDF aqui",
                type=['pdf'],
                help="Aceita apenas arquivos PDF"
            )
            st.markdown('</div>', unsafe_allow_html=True)
        else:
            st.markdown(
                '<div class="success-box">✨ Usando o artigo de exemplo: "The Perceptron: '
                'A Probabilistic Model for Information Storage and Organization in The Brain"</div>',
                unsafe_allow_html=True
            )
            uploaded_file = None
        st.markdown('</div>', unsafe_allow_html=True)

        # Botão de processamento
        st.markdown('<div class="section-spacing">', unsafe_allow_html=True)
        if st.button("🚀 Gerar Resumo", use_container_width=True):
            if not api_key:
                st.error('🔑 Por favor, insira sua chave API do Google')
                st.stop()
            
            if not uploaded_file and not use_sample:
                st.error('📁 Por favor, selecione um PDF ou use o exemplo')
                st.stop()

            try:
                with st.spinner('🔄 Analisando o documento...'):
                    if use_sample:
                        text_content = read_sample_pdf()
                        if text_content is None:
                            st.error("❌ Arquivo de exemplo não encontrado")
                            st.stop()
                    else:
                        pdf_reader = PyPDF2.PdfReader(uploaded_file)
                        text_content = ""
                        for page in pdf_reader.pages:
                            text_content += page.extract_text()
                    
                    if text_content.strip():
                        model = initialize_model(api_key)
                        response = summarize(text_content, model)
                        summarized_text = response.text

                        # Exibição do resultado
                        st.markdown('<div class="results-container">', unsafe_allow_html=True)
                        st.markdown(
                            '<h3 style="color: #1A1F36; margin-bottom: 1rem;">📝 Resumo Gerado</h3>',
                            unsafe_allow_html=True
                        )
                        st.markdown(summarized_text)
                        
                        # Botão de cópia
                        col1, col2 = st.columns([5,1])
                        with col2:
                            st_copy_to_clipboard(summarized_text)
                            st.caption("📋 Copiar")
                        st.markdown('</div>', unsafe_allow_html=True)
                        
            except Exception as e:
                st.error(f"❌ Erro ao processar o documento: {str(e)}")
                st.stop()
        st.markdown('</div>', unsafe_allow_html=True)

# Sidebar aprimorada
with st.sidebar:
    st.markdown('<div style="padding: 1rem;">', unsafe_allow_html=True)
    st.markdown(
        '<h3 style="color: #1A1F36; margin-bottom: 1rem;">ℹ️ Sobre o Projeto</h3>',
        unsafe_allow_html=True
    )
    st.write("""
    O Paper Summarizer utiliza a IA Generativa do Google para criar resumos 
    estruturados de artigos científicos, facilitando a compreensão rápida 
    dos principais pontos.
    """)
    
    st.markdown(
        '<h3 style="color: #1A1F36; margin: 1.5rem 0 1rem;">🎯 Como Usar</h3>',
        unsafe_allow_html=True
    )
    st.markdown("""
    1. 🔑 Insira sua chave API do Google
    2. 📄 Escolha entre usar o artigo de exemplo ou fazer upload do seu PDF
    3. 🚀 Clique em "Gerar Resumo"
    4. 📋 Copie o resultado gerado
    """)
    
    st.markdown("---")
    st.markdown(
        '<h3 style="color: #1A1F36; margin: 1.5rem 0 1rem;">👨‍💻 Desenvolvido por</h3>',
        unsafe_allow_html=True
    )
    st.markdown("[CLL](https://github.com/CllsPy)")
    st.markdown('</div>', unsafe_allow_html=True)