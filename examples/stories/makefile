all: stories.txt

stories.txt:
	curl -L "https://huggingface.co/datasets/roneneldan/TinyStories/resolve/main/TinyStories-valid.txt" -o $@
	sd --string-mode "<|endoftext|>" "" $@

clean:
	rm stories.txt
