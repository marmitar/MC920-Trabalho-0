% aga-homework.cls
%
% A LaTeX2e document class for preparing homework solutions.

% --- METADATA -----------------------------------------------------------------
\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{homework}

% --- OPTION PROCESSSING -------------------------------------------------------
\RequirePackage{kvoptions}
\SetupKeyvalOptions{
  family = homework,
  prefix = homework@
}

\DeclareStringOption[1]%
  {assignment}

% pass unrecognized options to `article` class
\DeclareDefaultOption{%
  \PassOptionsToClass{\CurrentOption}{article}%
}

% process all options
\ProcessKeyvalOptions{homework}

% load parent class with some default options
\LoadClass[a4paper, 11pt]{article}

\RequirePackage[portuguese]{babel}
\RequirePackage[T1]{fontenc}
\RequirePackage[utf8]{inputenc}
% --- PACKAGES AND SETUP -------------------------------------------------------
\RequirePackage[
    a4paper,
    headheight = 20pt,
    margin = 1in,
    tmargin = \dimexpr 1in - 10pt \relax
  ]{geometry} % set up nicer margins
  \addtolength{\footskip}{20pt}
\RequirePackage{fancyhdr} % for headers and footers
\RequirePackage{graphicx} % for including figures
\RequirePackage{mathpazo} % use Palation font
\RequirePackage{amsmath} % use AMS math package
\RequirePackage{amssymb} % use AMS symbols
\RequirePackage{amsthm} % for writing proofs
\RequirePackage{array} % for setting up arguments to columns
\RequirePackage{booktabs} % for professional tables
\RequirePackage{xcolor} % for colored text (comments in algorithms)
\RequirePackage{trimspaces, xstring} % for multiple author parsing
\RequirePackage[hidelinks]{hyperref}

\hypersetup{
  pdftitle  = {MC920 - Trabalho \homework@assignment},
  pdfauthor = {Tiago de Paula}
}

% look for figures in the figures directory
% \graphicspath{{figures/}}

% set up headers and footers; same for all pages
\setlength{\headheight}{14pt}
\fancyhf{}
\fancyhead[L]{\sffamily Universidade Estadual de Campinas}
\fancyhead[R]{\sffamily MC920 Processamento de Imagem Digital, 2020 2S}
\fancyfoot[L]{\sffamily Instituto de Computação}
\fancyfoot[R]{\sffamily\bfseries\thepage}
\renewcommand{\headrulewidth}{0.5pt}
\renewcommand{\footrulewidth}{0.5pt}
\pagestyle{fancy}

% ensure that the title is inserted in the document
\title{\vspace{-2\baselineskip}Trabalho \homework@assignment}
% \author{\aga@authorsProcessed}
\author{%
  Tiago de Paula Alves ~(187679) \\%
  \href{mailto:tiagodepalves@gmail.com}{\texttt{tiagodepalves@gmail.com}}%
}
\AtBeginDocument{\maketitle\thispagestyle{fancy}}
