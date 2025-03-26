import requests
import pandas as pd
import time


GITHUB_TOKEN = "insira o token"
REPO = "twbs/bootstrap"
HEADERS = {"Authorization": f"token {GITHUB_TOKEN}"}


ROLE_MAPPING = {
   "JavaScript": "Frontend",
   "TypeScript": "Frontend",
   "CSS": "Frontend",
   "HTML": "Frontend",
   "Sass": "Frontend",
   "Less": "Frontend",
   "Python": "Backend",
   "Jupyter Notebook": "Data Science",
   "R": "Data Science",
   "Java": "Backend",
   "C#": "Backend",
   "Go": "Backend",
   "PHP": "Backend",
   "Ruby": "Backend",
   "Swift": "Mobile",
   "Kotlin": "Mobile",
   "Objective-C": "Mobile",
   "Dart": "Mobile",
   "Shell": "DevOps",
   "Dockerfile": "DevOps",
   "Terraform": "DevOps",
   "PowerShell": "DevOps"
}


processed_developers = {}
processed_authors = set()


def get_commits_by_release(release_tag):
   url = f"https://api.github.com/repos/{REPO}/commits"
   params = {"sha": release_tag, "per_page": 100}
   response = requests.get(url, headers=HEADERS, params=params)


   if response.status_code == 401:
       print("❌ Erro: Token inválido! Verifique suas credenciais do GitHub.")
       exit(1)


   if response.status_code != 200:
       print(f"❌ Erro ao obter commits para {release_tag}: {response.json()}")
       return []


   commits = response.json()
   commit_data = []


   for commit in commits:
       author_login = commit["author"]["login"] if commit.get("author") and commit["author"].get("login") else None
       author_name = commit["commit"]["author"]["name"]
       commit_message = commit["commit"]["message"]


       author = author_login if author_login else author_name


       commit_data.append({
           "author": author,
           "commit_message": commit_message,
           "release": release_tag
       })


   return commit_data




def get_developer_info(username):
   if username in processed_developers:
       return processed_developers[username]


   url = f"https://api.github.com/users/{username}"
   response = requests.get(url, headers=HEADERS)


   if response.status_code == 404:
       print(f"⚠️ Usuário {username} não encontrado no GitHub.")
       return None


   if response.status_code != 200:
       print(f"❌ Erro ao obter usuário {username}")
       return None


   user_data = response.json()


   languages = get_developer_languages(username)
   profile = classify_developer(languages)


   dev_info = {
       "login": user_data.get("login"),
       "name": user_data.get("name"),
       "bio": user_data.get("bio"),
       "company": user_data.get("company"),
       "public_repos": user_data.get("public_repos"),
       "followers": user_data.get("followers"),
       "languages": languages,
       "perfil_tecnico": profile,
       "commit_messages": [],
       "releases": set()
   }


   processed_developers[username] = dev_info
   return dev_info




def get_developer_languages(username):
   url = f"https://api.github.com/users/{username}/repos"
   response = requests.get(url, headers=HEADERS, params={"per_page": 100})


   if response.status_code != 200:
       return []


   repos = response.json()
   lang_count = {}


   for repo in repos:
       lang = repo.get("language")
       if lang:
           lang_count[lang] = lang_count.get(lang, 0) + 1


   return sorted(lang_count.items(), key=lambda x: x[1], reverse=True)




def classify_developer(languages):
   roles = set()
   for lang, _ in languages:
       if lang in ROLE_MAPPING:
           roles.add(ROLE_MAPPING[lang])


   return ", ".join(roles) if roles else "Sem Classificação"




def analyze_releases(release_tags):
   all_commits = []


   for release_tag in release_tags:
       print(f"🔎 Analisando a release: {release_tag}...")


       commits = get_commits_by_release(release_tag)
       all_commits.extend(commits)


   for commit in all_commits:
       author = commit["author"]
       commit_message = commit["commit_message"]
       release_tag = commit["release"]


       print(f"📌 Coletando dados de {author}...")


       dev_info = get_developer_info(author)


       if dev_info:
           dev_info["commit_messages"].append(commit_message)
           dev_info["releases"].add(release_tag)


   for dev in processed_developers.values():
       dev["releases"] = ", ".join(sorted(dev["releases"]))
       dev["commit_messages"] = "; ".join(dev["commit_messages"])


   df = pd.DataFrame(processed_developers.values())


   print("\n📊 Análise Concluída!")
   print(df)


   if not df.empty:
       file_path = "insira o caminho que deseja salvar"
       df.to_csv(file_path, index=False, mode="w")
       print(f"\n📁 Relatório salvo como {file_path}")




release_input = input("Digite as releases separadas por vírgula (exemplo: v5.3.3, v5.2.0): ")
release_list = [r.strip() for r in release_input.split(",")]
analyze_releases(release_list)