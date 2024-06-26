﻿%
% Anhui University Thesis Template for Bachelorn
%
%   Based on：
%       USTC Thesis Template "USTC_Thesis_Bachelor_20120511" 
%           by XPS@USTC et al.
%
%   Created：
%       2014/03/06  yess@USTC, for my dearest CTT
%

\NeedsTeXFormat{LaTeX2e}[1994/12/01]
\ProvidesClass{ahnuthesis}[2014/03/06]

%去掉图表标题序号中的冒号
\newif\ifustc@CaptionNoColon\ustc@CaptionNoColonfalse
\DeclareOption{capnocolon}{\ustc@CaptionNoColontrue}

%章节标题格式以下三选一
%USTC中文格式
\newif\ifustc@TitleChinese\ustc@TitleChinesefalse
\DeclareOption{titlechinese}{\ustc@TitleChinesetrue}
%AHNU文科格式
\newif\ifahnu@TitleArt\ahnu@TitleArtfalse
\DeclareOption{titleahnuart}{\ahnu@TitleArttrue}
%AHNU理科格式
\newif\ifahnu@TitleScience\ahnu@TitleSciencefalse
\DeclareOption{titleahnuscience}{\ahnu@TitleSciencetrue}

%现在可以设置单面或者双面选项
\DeclareOption*{\PassOptionsToClass{\CurrentOption}{ctexbook}}
\ProcessOptions
\LoadClass[12pt,a4paper,fancyhdr,fntef]{ctexbook}

%%Packages
\RequirePackage{amsmath}
\RequirePackage{amsfonts}
\RequirePackage{amssymb}
\RequirePackage[integrals]{wasysym}
\RequirePackage{graphicx}
\RequirePackage[sort,numbers]{natbib}
\bibliographystyle{unsrtnat}%plainnat
\RequirePackage{longtable}
\RequirePackage{amsthm}
\RequirePackage{bbm}
\RequirePackage{bm}
\RequirePackage{indentfirst}
\RequirePackage{ifthen}
%\RequirePackage{titlesec}
\RequirePackage{caption3}
%\RequirePackage{floatrow}
\RequirePackage{hyperref}
%\RequirePackage{hypcap}
\RequirePackage{array}
\RequirePackage{subfigure}
\RequirePackage{xcolor}
\RequirePackage{multicol}
\RequirePackage{multirow}
\RequirePackage{fontspec}
%\RequirePackage{titletoc}

%Caption no colon
\ifustc@CaptionNoColon
  \def\fnum@figure#1{\figurename\nobreakspace\thefigure
    \hspace{0.5em}}
  \def\fnum@table#1{\tablename\nobreakspace\thetable
    \hspace{0.5em}}
\fi

%在正文中无论是否在图形环境中，用 \figcaption 均可得到图形标题
%同样，无论是否在表格环境中，用 \tabcaption 均可得到表格标题。
\newcommand\figcaption{\def\@captype{figure}\caption} \newcommand\tabcaption{\def\@captype{table}\caption}

%提供表格环境下p{width}加强版命令，使用L{width}等可以在指定宽度的同时指定对齐方式。
\newcommand{\PreserveBackslash}[1]{\let\temp=\\#1\let\\=\temp}
\newcolumntype{C}[1]{>{\PreserveBackslash\centering}p{#1}}
\newcolumntype{R}[1]{>{\PreserveBackslash\raggedleft}p{#1}}
\newcolumntype{L}[1]{>{\PreserveBackslash\raggedright}p{#1}}

%Superscript reference
\newcommand{\scite}[1]{\textsuperscript{\cite{#1}}}

%Chinese font size
\newcommand{\chuhao}{\fontsize{42pt}{\baselineskip}\selectfont}
\newcommand{\xiaochuhao}{\fontsize{36pt}{\baselineskip}\selectfont}
\newcommand{\yihao}{\fontsize{28pt}{\baselineskip}\selectfont}
\newcommand{\erhao}{\fontsize{21pt}{\baselineskip}\selectfont}
\newcommand{\xiaoerhao}{\fontsize{18pt}{\baselineskip}\selectfont}
\newcommand{\sanhao}{\fontsize{15.75pt}{\baselineskip}\selectfont}
\newcommand{\xiaosanhao}{\fontsize{15pt}{\baselineskip}\selectfont}
\newcommand{\sihao}{\fontsize{14pt}{\baselineskip}\selectfont}
\newcommand{\xiaosihao}{\fontsize{12pt}{\baselineskip}\selectfont}
\newcommand{\wuhao}{\fontsize{10.5pt}{\baselineskip}\selectfont}
\newcommand{\xiaowuhao}{\fontsize{9pt}{\baselineskip}\selectfont}
\newcommand{\liuhao}{\fontsize{7.875pt}{\baselineskip}\selectfont}
\newcommand{\qihao}{\fontsize{5.25pt}{\baselineskip}\selectfont}

%autoref option of hyperref
\def\equationautorefname{式}%
\def\footnoteautorefname{脚注}%
\def\itemautorefname{项}%
\def\figureautorefname{图}%
\def\subfigureautorefname{图}%
\def\tableautorefname{表}%
\def\partautorefname{篇}%
\def\appendixautorefname{附录}%
\def\chapterautorefname{章}%
\def\sectionautorefname{节}%
\def\subsectionautorefname{小节}%
%\def\paragraphautorefname{段落}%
%\def\subparagraphautorefname{子段落}%
%\def\FancyVerbLineautorefname{行}%
\def\theoremautorefname{定理}%
\def\assumptionautorefname{假设}
\def\propertyautorefname{性质}%

%Titlepage %USTC style 
\newcommand*{\titletail}[1]{\gdef\@titletail{#1}}
\newcommand*{\tutor}[1]{\gdef\@tutor{#1}}
\newcommand*{\entitle}[1]{\gdef\@entitle{#1}}
\newcommand*{\enauthor}[1]{\gdef\@enauthor{#1}}
\newcommand*{\entutor}[1]{\gdef\@entutor{#1}}
\newcommand*{\cntime}[1]{\gdef\@cntime{#1}}
\newcommand*{\entime}[1]{\gdef\@entime{#1}}
\global\let\@titletail\@empty
\global\let\@entitle\@empty
\global\let\@tutor\@empty
\global\let\@enauthor\@empty
\global\let\@entutor\@empty
\global\let\@cntime\@empty
\global\let\@entime\@empty
\newcommand*{\department}[1]{\gdef\@department{#1}}
\newcommand*{\No}[1]{\gdef\@No{#1}}
\global\let\@department\@empty
\global\let\@No\@empty
\renewcommand\maketitle{%
  \newpage
  \thispagestyle{empty}
  \null
  \begin{center}%
    \let \footnote \thanks
    {\Huge \textit{安徽师范大学}\\
      \Large \textrm{Anhui Normal University}\\
      \Huge \textit{本科毕业论文}\\ \Large\textrm{A Dissertation for the Bachelor's Degree} \par}%
    \vskip 1.5cm
    \sihao\@title\ifx\@titletail\@empty\else\@titletail\fi
    \\
    \sihao\@entitle
    {\large
    \lineskip .5em%
    \\
    \vskip2.5cm
    {
    \renewcommand\arraystretch{1.2}
    \begin{tabular}[t]{cc}%
      姓$\quad$名      & \underline{\makebox[6cm][c]{\@author}}   \\
      B.S. Candidate & \underline{\makebox[6cm][c]{\@enauthor}} \\
      导$\quad$师      & \underline{\makebox[6cm][c]{\@tutor}}    \\
      Supervisor     & \underline{\makebox[6cm][c]{\@entutor}}  \\
    \end{tabular}}\par}%
    \vskip3em
    {\Large\@cntime}\\
    {\Large\@entime}
  \end{center}
  \newpage\thispagestyle{empty}\renewcommand\arraystretch{1.0}
}

%define a new title style %一种中英分为两页的扉页形式，需要校徽图案，AHNU不适用
\newcommand\makeseparatetitle{%
  \newpage
  \thispagestyle{empty}
  \null
  \begin{center}%
    {\includegraphics[scale=0.3]{ahnu_name.jpg}\\\yihao{~}\\
      \yihao \textit{学士学位论文}\\  \par}%
    \vskip 0.5cm
    \ifx\@titletail\@empty\vskip 0.5cm\else\fi
    \includegraphics[scale=0.3]{ahnu_logo.jpg}
    {\large
      \lineskip .5em%
      \\
      \vskip 0.5cm
      \ifx\@titletail\@empty\vskip 0.5cm\else\fi
      {
        \renewcommand\arraystretch{1.2}
        \begin{tabular}[t]{cc}%
          \heiti{题$\quad$目} & \underline{\makebox[8cm][c]{\@title}}\tabularnewline
          \ifx\@titletail\@empty\else
                            & \underline{\makebox[8cm][c]{\@titletail}}\tabularnewline
          \fi
          \heiti{院$\quad$系} & \underline{\makebox[8cm][c]{\@department}}\tabularnewline
          \heiti{姓$\quad$名} & \underline{\makebox[8cm][c]{\@author}}\tabularnewline
          \heiti{学$\quad$号} & \underline{\makebox[8cm][c]{\@No}}\tabularnewline
          \heiti{导$\quad$师} & \underline{\makebox[8cm][c]{\@tutor}}\tabularnewline
        \end{tabular}}\par}%
    \vskip3em
    {\Large\@cntime}
  \end{center}
  \newpage
  \thispagestyle{empty}
  \null
  \begin{center}%
    \let \footnote \thanks
    {\LARGE \textrm{Anhui Normal University}\\\vskip 0.5cm
      \Large\textrm{A Dissertation for the Bachelor's Degree}\\  \par}%
    \vskip 1cm
    \includegraphics[scale=0.3]{ahnu_logo.jpg}
    \vskip 1cm
    \sanhao\@entitle
    {\large
      \lineskip .5em%
      \\
      \vskip1cm
      {
        \renewcommand\arraystretch{1.2}
        \begin{tabular}[t]{cc}%
          B.S. Candidate & \underline{\makebox[6cm][c]{\@enauthor}} \\
          Supervisor     & \underline{\makebox[6cm][c]{\@entutor}}  \\
        \end{tabular}}\par}%
    \vskip3em
    {\Large Wuhu, Anhui 241000, China\\\@entime}
  \end{center}
  \newpage\renewcommand\arraystretch{1.0}
}

%coverpage  
\newcommand\makecover{
  \thispagestyle{empty}
  \newgeometry{top=17.4cm,bottom=1.1cm,left=6cm,right=5.5cm}
  {\vspace*{-0.8cm}\fontsize{17pt}{\baselineskip}\selectfont\bf\centering
    \setlength{\baselineskip}{1.1cm}
    \begin{minipage}[t][2.3cm][t]{9.8cm}
      \begin{center}
        \setlength{\baselineskip}{1.1cm}
        \@title\ifx\@titletail\@empty\else\@titletail\fi
      \end{center}
    \end{minipage}\\
    \begin{minipage}[t][3.05cm][t]{9.8cm}
      \setlength{\baselineskip}{1.05cm}
      \begin{center}
        \@entitle
      \end{center}
    \end{minipage}\\
    \setlength{\baselineskip}{1.1cm}
    \begin{minipage}[t][0.95cm][t]{9.8cm}
      \begin{center}
        \@department
      \end{center}
    \end{minipage}\\
    \begin{minipage}[t][0.95cm][t]{9.8cm}
      \begin{minipage}{3.63cm}
        \begin{center}
          \@author
        \end{center}
      \end{minipage}
      \hfill
      \begin{minipage}{3.82cm}
        \begin{center}
          \@No
        \end{center}
      \end{minipage}
    \end{minipage}\\
    \begin{minipage}[t][2.2cm][t]{9.8cm}
      \setlength{\baselineskip}{1cm}
      \begin{center}
        \@tutor\\
        \@cntime
      \end{center}
    \end{minipage}
  }
  \newpage\restoregeometry
}

%Titlepage, AHNU style
\newcommand*{\major}[1]{\gdef\@major{#1}}
\newcommand*{\enrolltime}[1]{\gdef\@enrolltime{#1}}
\newcommand*{\tutordegree}[1]{\gdef\@tutordegree{#1}}
\newcommand*{\sumwords}[1]{\gdef\@sumwords{#1}}
\newcommand*{\tutordepartment}[1]
{\gdef\@tutordepartment{#1}}
\global\let\@major\@empty
\global\let\@enrolltime\@empty
\global\let\@tutordegree\@empty
\global\let\@tutordepartment\@empty
\global\let\@sumwords\@empty
\newcommand\makeahnutitle{%
  \newpage
  \thispagestyle{empty}
  \null
  \begin{center}%
    {\includegraphics[scale=0.2]{ahnu_name.jpg}\\\vskip 1cm
      \xiaochuhao\songti\textbf{本科学生毕业论文(设计)}\\ \par}%
    \vskip 5cm
    \ifx\@titletail\@empty\vskip 1cm\else\fi
    {\large
      \lineskip .5em%
        {
          \renewcommand\arraystretch{1.2}
          \begin{tabular}[t]{llrr}%
            \songti\textbf{题$\quad$目：}
                                       & \multicolumn{3}{l}{\underline{\makebox[10cm][c]{\@title}}}\tabularnewline
            \ifx\@titletail\@empty\else
                                       & \multicolumn{3}{l}{\underline{\makebox[10cm][c]{\@titletail}}}\tabularnewline
            \fi
            \songti\textbf{学$\quad$院：} & \multicolumn{3}{l}{\underline{\makebox[10cm][c]{\@department}}}
            \tabularnewline
            \songti\textbf{专$\quad$业：} & \multicolumn{3}{l}{\underline{\makebox[10cm][c]{\@major}}}
            \tabularnewline
            \songti\textbf{学生姓名：}      & \multicolumn{3}{l}{\underline{\makebox[10cm][c]{\@author}}}
            \tabularnewline
            \songti\textbf{学$\quad$号：} & \multicolumn{3}{l}{\underline{\makebox[10cm][c]{\@No}}}
            \tabularnewline
            \songti\textbf{指导教师：}      & \underline{\makebox[3.5cm][c]{\@tutor}}
                                       & \songti\textbf{职$\quad$称：}                                                    & \underline{\makebox[3cm][c]{\@tutordegree}}\tabularnewline
            \songti\textbf{论文字数：}      & \multicolumn{3}{l}{\underline{\makebox[10cm][c]{\@sumwords}}}
            \tabularnewline
            \tabularnewline
            \tabularnewline
            \songti\textbf{完成日期：}      & \multicolumn{3}{l}{\underline{\makebox[10cm][c]{\@cntime}}}\tabularnewline
          \end{tabular}}\par}%
  \end{center}
  \newpage\renewcommand\arraystretch{1.0}
}


%%Page Setup
\RequirePackage[
  includeheadfoot,
  top=2.5cm, bottom=2.0cm,
  headsep=0.6cm,
  headheight=0.6cm,
  footnotesep=0.8cm,
  footskip=1cm,
  textheight=22.5cm,
  hmargin=2.0cm,
  bindingoffset=0.5cm
  %twosideshift=0 pt,
]{geometry}


%lengths
\setlength{\parindent}{2\ccwd}
\setlength{\parskip}{0pt}
\setlength{\baselineskip}{20pt}
\setlength{\headsep}{1 cm}
\setlength{\textwidth}{16.5true cm}
\setlength{\belowcaptionskip}{0pt}
%\setlength{\abovecaptionskip}{0pt}

%titleformat
%\titleformat{\section}{\center\bfseries\xiaosanhao}{\thesection}{1em}{}
%\titleformat{\subsection}{\flushleft\bfseries\sihao}{\thesubsection}{1em}{}
%\titleformat{\subsubsection}{\flushleft\bfseries\sihao}{\thesubsubsection}{1em}{}
%\titleformat{\chapter}{\centering\sanhao\bfseries}{第\,\thechapter\,章}{1em}{}
%\titlespacing{\chapter}{0cm}{-.9cm}{.4cm}
%\renewcommand{\thesubsubsection}{\arabic{subsubsection}.}


\CTEXoptions[listfigurename={插图索引}]
\CTEXoptions[listtablename={表格索引}]

\ifustc@TitleChinese
  \CTEXsetup[format={{\centering\sanhao\bfseries}}]{chapter}
  \CTEXsetup[format={{\center\bfseries\xiaosanhao}}]{section}
  \CTEXsetup[format={{\flushleft\bfseries\sihao}}]{subsection}
  \CTEXsetup[format={{\flushleft\bfseries\xiaosihao}}]{subsubsection}
  \CTEXsetup[number={\chinese{chapter}}]{chapter}
  \CTEXsetup[number={\chinese{section}}]{section}
  \CTEXsetup[number={\chinese{subsection}}]{subsection}
  \CTEXsetup[number={\arabic{subsubsection}}]{subsubsection}
  \CTEXsetup[number={\arabic{paragraph}}]{paragraph}
  \CTEXsetup[name={第,章}]{chapter}
  \CTEXsetup[name={第,节}]{section}
  \CTEXsetup[name={,、}]{subsection}
  \CTEXsetup[name={,}]{subsubsection}
  \CTEXsetup[name={(,)}]{paragraph}
\fi

\ifahnu@TitleArt
  %\CTEXsetup[format={{\centering\heiti\xiaosihao\bfseries}}]{chapter}
  %不知道为什么上面这行不管用，所以用下面两行代替
  \CTEXsetup[nameformat={{\centering\heiti\xiaosihao\bfseries}}]{chapter}
  \CTEXsetup[titleformat={{\centering\heiti\xiaosihao\bfseries}}]{chapter}
  \CTEXsetup[format={{\songti\xiaosihao\bfseries}}]{section}
  \CTEXsetup[format={{\songti\xiaosihao}}]{subsection}
  \CTEXsetup[format={{\songti\xiaosihao}}]{subsubsection}
  \CTEXsetup[format={{\songti\xiaosihao}}]{paragraph}
  \CTEXsetup[beforeskip={0.1pt}]{chapter}
  \CTEXsetup[beforeskip={0.1pt}]{section}
  \CTEXsetup[beforeskip={0.1pt}]{subsection}
  \CTEXsetup[beforeskip={0.1pt}]{subsubsection}
  \CTEXsetup[beforeskip={0.1pt}]{paragraph}
  \CTEXsetup[afterskip={1pt}]{chapter}
  \CTEXsetup[afterskip={0.01pt}]{section}
  \CTEXsetup[afterskip={0.01pt}]{subsection}
  \CTEXsetup[afterskip={0.01pt}]{subsubsection}
  \CTEXsetup[afterskip={0.01pt}]{paragraph}
  \CTEXsetup[indent={2\ccwd}]{section}
  \CTEXsetup[indent={2\ccwd}]{subsection}
  \CTEXsetup[indent={2\ccwd}]{subsubsection}
  \CTEXsetup[indent={2\ccwd}]{paragraph}
  \CTEXsetup[number={\chinese{chapter}}]{chapter}
  \CTEXsetup[number={\chinese{section}}]{section}
  \CTEXsetup[number={\arabic{subsection}}]{subsection}
  \CTEXsetup[number={\arabic{subsubsection}}]{subsubsection}
  \CTEXsetup[number={\textcircled{\tiny{\arabic{paragraph}}}}]{paragraph}
  \CTEXsetup[name={,、}]{chapter}
  \CTEXsetup[name={（,）}]{section}
  \CTEXsetup[name={,、}]{subsection}
  \CTEXsetup[name={(,)}]{subsubsection}
  \CTEXsetup[name={,}]{paragraph}
\fi

\ifahnu@TitleScience
  %\CTEXsetup[format={{\flushleft\songti\xiaosihao\bfseries}}]{chapter}
  \CTEXsetup[nameformat={{\songti\xiaosihao\bfseries}}]{chapter}
  \CTEXsetup[titleformat={{\songti\xiaosihao\bfseries}}]{chapter}
  \CTEXsetup[format={{\songti\xiaosihao\bfseries}}]{section}
  \CTEXsetup[format={{\songti\xiaosihao}}]{subsection}
  \CTEXsetup[format={{\songti\xiaosihao}}]{subsubsection}
  \CTEXsetup[format={{\songti\xiaosihao}}]{paragraph}
  \CTEXsetup[beforeskip={0.1pt}]{chapter}
  \CTEXsetup[beforeskip={0.1pt}]{section}
  \CTEXsetup[beforeskip={0.1pt}]{subsection}
  \CTEXsetup[beforeskip={0.1pt}]{subsubsection}
  \CTEXsetup[afterskip={0.1pt}]{chapter}
  \CTEXsetup[afterskip={0.1pt}]{section}
  \CTEXsetup[afterskip={0.1pt}]{subsection}
  \CTEXsetup[afterskip={0.1pt}]{subsubsection}
  \CTEXsetup[number={\arabic{chapter}}]{chapter}
  \CTEXsetup[name={,}]{chapter}
  \CTEXsetup[aftername={$\quad$}]{chapter}
  \CTEXsetup[aftername={$\quad$}]{section}
  \CTEXsetup[aftername={$\quad$}]{subsection}
  \CTEXsetup[aftername={$\quad$}]{subsubsection}
\fi


%headings
\pagestyle{fancy}
\fancyhf{}
\fancyhead[C]{\fontsize{9pt}{\baselineskip}\selectfont 安徽师范大学本科毕业论文}
\fancyhead[L,R]{}
\fancyfoot[C]{\thepage}
\let\ps@plain\ps@fancy

%theorems 
\newtheorem{theorem}{\textbf{\hspace{0.7pt}定理}}[section]
\newtheorem{lemma}{\textbf{\hspace{0.7pt}引理}}[section]
\newtheorem{example}{\textbf{\hspace{0.7pt}例}}[section]
\newtheorem{algorithm}{\textbf{\hspace{0.7pt}算法}}[section]
\newtheorem{definition}{\textbf{\hspace{0.7pt}定义}}[section]
\newtheorem{axiom}{\textbf{\hspace{0.7pt}公理}}[section]
\newtheorem{property}{\textbf{\hspace{0.7pt}性质}}[section]
\newtheorem{proposition}{\textbf{\hspace{0.7pt}命题}}[section]
\newtheorem{corollary}{\textbf{\hspace{0.7pt}推论}}[section]
\newtheorem{remark}{\textbf{\hspace{0.7pt}注解}}[section]
\newtheorem{condition}{\textbf{\hspace{0.7pt}条件}}[section]
\newtheorem{conclusion}{\textbf{\hspace{0.7pt}结论}}[section]
\newtheorem{assumption}{\textbf{\hspace{0.7pt}假设}}[section]
\newtheorem{prove}{\textbf{\hspace{0.7pt}证明}}[section]
\renewcommand\appendixname{附录}
\renewcommand{\proofname}{证明}

%upStand Greek Letters
\DeclareMathSymbol{\upGamma}{\mathord}{operators}{0}
\DeclareMathSymbol{\upDelta}{\mathord}{operators}{1}
\DeclareMathSymbol{\upTheta}{\mathord}{operators}{2}
\DeclareMathSymbol{\upLambda}{\mathord}{operators}{3}
\DeclareMathSymbol{\upXi}{\mathord}{operators}{4}
\DeclareMathSymbol{\upPi}{\mathord}{operators}{5}
\DeclareMathSymbol{\upSigma}{\mathord}{operators}{6}
\DeclareMathSymbol{\upUpsilon}{\mathord}{operators}{7}
\DeclareMathSymbol{\upPhi}{\mathord}{operators}{8}
\DeclareMathSymbol{\upPsi}{\mathord}{operators}{9}
\DeclareMathSymbol{\upOmega}{\mathord}{operators}{10}

%Misc Customization
\renewcommand{\theequation}{\arabic{chapter}-\arabic{equation}}
\setcounter{secnumdepth}{4}
%\captionfont{\xiaosihao\rm}
\def\rmd{\mathrm{d}}
\def\rmi{\mathrm{i}}
\def\rme{\mathrm{e}}

%tableofcontents
\renewcommand{\contentsname}{目$\quad$录}
\renewcommand\tableofcontents{%
  \if@twocolumn
    \@restonecoltrue\onecolumn
  \else
    \@restonecolfalse
  \fi
  \centerline{{\xiaoerhao\bfseries\contentsname}
    \@mkboth{%
      \MakeUppercase\contentsname}{\MakeUppercase\contentsname}}%
  \@starttoc{toc}%
  \if@restonecol\twocolumn\fi
}

%Special Pages
\newcommand*{\keywords}[1]{\gdef\@keywords{#1}}
\newcommand*{\cnkeywords}[1]{\gdef\@cnkeywords{#1}}
\global\let\@keywords\@empty
\global\let\@cnkeywords\@empty
\newcommand{\thankspagename}{致$\quad$谢}

\newenvironment{thankspage}{%
  \newpage
  \if@twocolumn
    \section*{\thankspagename}%
  \else
    \small
    \chapter*{~}
    \vspace{-150pt}
    \begin{center}%
      \phantomsection
      \addcontentsline{toc}{chapter}{\texorpdfstring{致$\quad$谢}{致谢}}
      \setlength{\baselineskip}{20pt}
      \vskip 4.5cm
        %{\bfseries\xiaoerhao \thankspagename\vspace{-.5em}\vspace{\z@}}%
        {\bfseries\sihao\heiti \thankspagename}%      
    \end{center}%
    \xiaosihao\songti\quotation
  \fi}
{\if@twocolumn\else\endquotation\cleardoublepage\fi}


%Pdfinfo Setup
\renewcommand\@pdfauthor{\@author}
\renewcommand\@pdftitle{\@title\ifx\@titletail\@empty\else\@titletail\fi}
\renewcommand\@pdfsubject{安徽师范大学本科毕业论文}
\hypersetup{%
  pdfstartview = FitH,}

%table setup, by Heavenseven
\newcolumntype{I}{!{\vrule width 1pt}}
\newlength\savedwidth
\newcommand\whline{\noalign{\global\savedwidth\arrayrulewidth
    \global\arrayrulewidth 1pt}%
  \hline
  \noalign{\global\arrayrulewidth\savedwidth}}


%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%code environment, from ctex-faq
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\definecolor{example@bkcolor}{gray}{.875}
%
\newwrite\example@out
\def\example@start{%
  \begingroup% Lets Keep the Changes Local
  \@bsphack
  \immediate\openout \example@out \jobname.exa
  \let\do\@makeother\dospecials\catcode`\^^M\active
  \def\verbatim@processline{%
    \immediate\write\example@out{\the\verbatim@line}}%
  \verbatim@start}
\def\example@finish{\immediate\closeout\example@out\@esphack\endgroup}
\def\example@code#1#2{%
  \colorbox{#1}{%
    \begin{minipage}[c]{#2}%
      \small\verbatiminput{\jobname.exa}%
    \end{minipage}%
  }%
}
\def\example@output#1{%
  \let\savefboxrule\fboxrule%
  \let\savefboxsep\fboxsep%
  \setlength{\fboxrule}{0.1pt}%
  \setlength{\fboxsep}{3mm}%
  \fbox{%
    \begin{minipage}[c]{#1}%
      \setlength{\fboxrule}{\savefboxrule}%
      \setlength{\fboxsep}{\savefboxsep}%
      \setlength{\parskip}{1ex plus 0.4ex minus 0.2ex}%
      \begin{trivlist}\item\small\input{\jobname.exa}\end{trivlist}
    \end{minipage}
  }%
}
\newenvironment{code}%
{\example@start}%
{\example@finish%
  \list{}{\itemindent-\leftmargin}\item\relax%
  \makebox[\textwidth][c]{%
    \example@code{example@bkcolor}{0.96\textwidth}%
  }%
  \endlist}
